let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs:[
        { className: "centered", targets:[0, 1, 2, 3, 4, 5] },
        { orderable: false, targets:[3, 4, 5] },
        { searchable: false, targets:[5] },
        { width: '10%', targets: 5 }  // Define el ancho de la segunda columna al 30%

    ],
    pageLength: 6,
    destroy: true
}

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
        dataTable = null; // Limpia la referencia a la instancia de DataTable
    }
    await listProceedings();

    dataTable = $('#datatable-proceedings').DataTable(Object.assign({}, dataTableOptions, {
        language: {
            search: "Buscar:",
            zeroRecords: "No se encontraron registros coincidentes",
            info: "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            infoEmpty: "Mostrando registros del 0 al 0 de un total de 0 registros",
            infoFiltered: "(filtrado de un total de _MAX_ registros)",
            lengthMenu: "",
            paginate: {
                first: "Primero",
                previous: "Anterior",
                next: "Siguiente",
                last: "Último"
            }
        }
    }));
    dataTableIsInitialized = true;
}


const listProceedings = async () => {
    try{
        const response = await fetch('/expedientes/list_proceedings/');
        const data = await response.json();
        let content = ``;

        data.proceedings.forEach((proceeding)=>{
            let updateURL = `editar/${proceeding.id}`;
            let deleteURL = `eliminar?pid=${proceeding.id}`;
            let banfeURL = `../banfe/?pid=${proceeding.id}`;
            content+=`
                <tr>
                    <td>${proceeding.name+" "+proceeding.first_last_name+" "+proceeding.second_last_name}</td>
                    <td>${calculateAge(proceeding.dateNac)}</td>
                    <td>${proceeding.scholarship}</td>
                    <td>${proceeding.gender}</td>
                    <td>${proceeding.reason_consultation}</td>
                    <td class="options-btn">
                        <a href="${updateURL}" class='btn btn-sm btn-warning'><i class='dt-icons fa-solid fa-pencil'></i></a>
                        <a href="${deleteURL}" class='btn btn-sm btn-danger'><i class='dt-icons fa-solid fa-trash-can'></i></a>
                    </td>
                    <td class="options-btn">
                        <a href="${banfeURL}" class='btn btn-sm btn-success'><i class='dt-icons text-light fa-solid fa-magnifying-glass-chart'></i></a>
                    </td>
                </tr>
            `;
        });
        tableBody_proceedings.innerHTML = content;
    }catch(e){
        alert(e);
    }
};

window.addEventListener('load', async()=>{
    await initDataTable();
})

//  Función que calcula la edad del sujeto a partir de su fecha de nacimiento
const calculateAge = (dateBirth) => {
    const dateNow = new Date();
    const yearNow = parseInt(dateNow.getFullYear());
    const monthNow = parseInt(dateNow.getMonth()) + 1;
    const dayNow = parseInt(dateNow.getDate());
  
    const yearBirth = parseInt(String(dateBirth).substring(0, 4));
    const monthBirth = parseInt(String(dateBirth).substring(5, 7));
    const dayBirth = parseInt(String(dateBirth).substring(8, 10));
  
    let age = yearNow - yearBirth;
  
    if (monthNow < monthBirth) {
      age--;
    } else if (monthNow === monthBirth) {
      if (dayNow < dayBirth) {
        age--;
      }
    }
  
    return age;
  };