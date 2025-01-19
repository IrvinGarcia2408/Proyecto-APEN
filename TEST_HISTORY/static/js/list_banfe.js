let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
  columnDefs: [
    { className: "centered", targets: "_all" },
    { orderable: false, targets: [3, 4, 5] },
    { searchable: false, targets: [5] },
    { width: "20%", targets: 0 }, // Define el ancho de la primera columna al 20%
    { width: "15%", targets: [1,2,3] }, // Define el ancho de la primeras columnas al 15%
  ],
  pageLength: 5,
  destroy: true,
};

const initDataTable = async () => {
  if (dataTableIsInitialized) {
    dataTable.destroy();
    dataTable = null; // Limpia la referencia a la instancia de DataTable
  }
  await listTests();

  dataTable = $("#datatable-tests").DataTable(
    Object.assign({}, dataTableOptions, {
      language: {
        search: "Buscar:",
        zeroRecords: "No se encontraron registros coincidentes",
        info: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
        infoFiltered: "(filtrado de un total de _MAX_ registros)",
        lengthMenu: "",
        exportOptions: {
                modifier: {
                    page: 'all' // Esto asegura que se exporten todas las filas, no solo las visibles
                }
            },
        paginate: {
          first: "Primero",
          previous: "Anterior",
          next: "Siguiente",
          last: "Último",
        },
      },
    })
  );
  dataTableIsInitialized = true;
};

const listTests = async () => {
  try {
    const response = await fetch("/pruebas/list_tests/");
    const data = await response.json();
    let content = ``;

    data.forEach((tests_data) => {
      tests_data.banfe_results.forEach((banfe) => { // Itera sobre cada BANFE
        let testURL = `edit_banfe?banfe=${banfe.banfe_id}`;
        let resultURL = `details_banfe?banfe=${banfe.banfe_id}`;

        content += `
          <tr>
            <td>${tests_data["proceeding_name"]}</td>
            <td class="${
              banfe.diagnosis_orbitomedial === "ALTERACIÓN MODERADA"
                ? "orange-text"
                : banfe.diagnosis_orbitomedial === "NORMAL ALTO"
                ? "green-text"
                : banfe.diagnosis_orbitomedial === "NORMAL"
                ? "blue-text"
                : banfe.diagnosis_orbitomedial === "ALTERACIÓN SEVERA"
                ? "red-text"
                : ""
            }">
              ${banfe.diagnosis_orbitomedial}
            </td>
            <td class="${
              banfe.diagnosis_prefrontal === "ALTERACIÓN MODERADA"
                ? "orange-text"
                : banfe.diagnosis_prefrontal === "NORMAL ALTO"
                ? "green-text"
                : banfe.diagnosis_prefrontal === "NORMAL"
                ? "blue-text"
                : banfe.diagnosis_prefrontal === "ALTERACIÓN SEVERA"
                ? "red-text"
                : ""
            }">
              ${banfe.diagnosis_prefrontal}
            </td>
            <td class="${
              banfe.diagnosis_dorsolateral === "ALTERACIÓN MODERADA"
                ? "orange-text"
                : banfe.diagnosis_dorsolateral === "NORMAL ALTO"
                ? "green-text"
                : banfe.diagnosis_dorsolateral === "NORMAL"
                ? "blue-text"
                : banfe.diagnosis_dorsolateral === "ALTERACIÓN SEVERA"
                ? "red-text"
                : ""
            }">
              ${banfe.diagnosis_dorsolateral}
            </td>
            <td class="${
              banfe.diagnosis_total === "ALTERACIÓN MODERADA"
                ? "orange-text"
                : banfe.diagnosis_total === "NORMAL ALTO"
                ? "green-text"
                : banfe.diagnosis_total === "NORMAL"
                ? "blue-text"
                : banfe.diagnosis_total === "ALTERACIÓN SEVERA"
                ? "red-text"
                : ""
            }">
              ${banfe.diagnosis_total}
            </td>
            <td class="options-btn">
              <a href="${testURL}" class='btn btn-sm btn-warning'><i class='dt-icons fa-solid fa-pencil'></i></a>
              <a href="${resultURL}" class='btn btn-sm btn-info'><i class="dt-icons fa-solid fa-eye"></i></a>
            </td>
            <td class="options-btn">
              <input type="checkbox" class="individualCheckbox" id="cbox_${banfe.banfe_id}" value="Si" />                        
            </td>
          </tr>
        `;
      });
    });

    tableBody_tests.innerHTML = content;
    addCheckboxEventListeners();
  } catch (e) {
    alert(e);
  }
};

const addCheckboxEventListeners = () => {
  const selectAllCheckbox = document.getElementById("cbox_all");
  const checkboxes = document.querySelectorAll(".individualCheckbox");

  selectAllCheckbox.addEventListener("change", function () {
    checkboxes.forEach((checkbox) => {
      checkbox.checked = selectAllCheckbox.checked;
    });
  });

  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      if (!checkbox.checked) {
        selectAllCheckbox.checked = false;
      } else {
        const allChecked = Array.from(checkboxes).every(
          (checkbox) => checkbox.checked
        );
        selectAllCheckbox.checked = allChecked;
      }
    });
  });
};

window.addEventListener("load", async () => {
  await initDataTable();
});

document
  .getElementById("exportSelectedTests")
  .addEventListener("click", async () => {
    console.log("Botón de exportación de pruebas seleccionadas clickeado");

    const checkboxes = $('#datatable-tests')
    .DataTable()
    .rows({ search: 'applied' }) // Filtra según la búsqueda actual
    .nodes() // Obtiene todas las filas visibles y no visibles
    .to$() // Convierte a jQuery para manipulación
    .find('input[type="checkbox"]:checked'); // Encuentra todos los checkboxes seleccionados
  
    console.log("Número de checkboxes seleccionados:", checkboxes.length);

    const selectedIds = Array.from(checkboxes).map(
      (checkbox) => checkbox.id.split("_")[1]
    );
    console.log("IDs seleccionados:", selectedIds);

    if (selectedIds.length === 0) {
      alert("No se ha seleccionado ninguna prueba.");
      return;
    }

    const formData = new FormData();
    selectedIds.forEach((id) => formData.append("test_ids[]", id));

    console.log(
      "FormData creado:",
      Array.from(formData.entries())
        .map((entry) => entry.join(": "))
        .join(", ")
    );
    for (let pair of formData.entries()) {
      console.log(pair[0] + ": " + pair[1]);
    }

    try {
      const response = await fetch("export_selected_tests_csv/", {
        method: "POST",
        body: formData,
      });

      console.log("Respuesta del servidor recibida");

      if (response.ok) {
        console.log("Respuesta OK");
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "selected_tests.csv";
        document.body.appendChild(a);
        a.click();
        a.remove();
      } else {
        alert("Hubo un problema al exportar las pruebas.");
        const responseText = await response.text();
        console.error("Respuesta del servidor:", responseText);
      }
    } catch (error) {
      console.error("Error al realizar la petición:", error);
      alert("Error al realizar la petición: " + error.message);
    }
  });
