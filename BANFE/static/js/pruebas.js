// Función que calcula la edad del sujeto a partir de su fecha de nacimiento
const calculateAge = (dateBirth) => {
  // Obtiene la fecha actual
  const dateNow = new Date();
  // Obtiene el año actual
  const yearNow = dateNow.getFullYear();
  // Obtiene el mes actual y suma 1 porque los meses se indexan desde 0
  const monthNow = dateNow.getMonth() + 1;
  // Obtiene el día actual
  const dayNow = dateNow.getDate();

  // Obtiene el año de nacimiento
  const yearBirth = parseInt(dateBirth.substring(0, 4));
  // Obtiene el mes de nacimiento
  const monthBirth = parseInt(dateBirth.substring(5, 7));
  // Obtiene el día de nacimiento
  const dayBirth = parseInt(dateBirth.substring(8, 10));

  // Calcula la edad restando el año actual al año de nacimiento
  let age = yearNow - yearBirth;

  // Ajusta la edad si el mes actual es menor que el mes de nacimiento
  if (monthNow < monthBirth) {
    age--;
  } else if (monthNow === monthBirth) { // Si el mes actual es igual al mes de nacimiento
    // Verifica si el día actual es menor que el día de nacimiento
    if (dayNow < dayBirth) {
      age--; // Reduce la edad en 1
    }
  }

  // Devuelve la edad calculada
  return age;
};

// Espera a que el contenido del DOM esté completamente cargado antes de ejecutar el script
document.addEventListener("DOMContentLoaded", function () {

  // Obtener referencias a elementos del DOM
  var search = document.getElementById("search_option");
  var initEvaluation = document.getElementById("startEvaluation");

  // Deshabilitar el campo de edad
  document.getElementById("age_subject").disabled = true;

  // Borrar opciones anteriores del elemento select 'search_option' y añadir la opción 'Todos'
  search.innerHTML = "<option value='Todos'>Todos</option>";

  // Verificar si hay un procedimiento seleccionado
  if (document.getElementById("proceeding_id").value != -1) {
    // Si hay un procedimiento seleccionado, establecer el valor del nombre del sujeto y calcular la edad
    var nameSubject = document.getElementById("name_subject");
    nameSubject.value = document.getElementById("proceeding_id").value;
    document.getElementById("age_subject").value = calculateAge(
      document.getElementById("date_subject").value
    );
    // Habilitar el botón de inicio de la evaluación
    initEvaluation.classList.remove("disabled");
  } else {
    // Si no hay un procedimiento seleccionado, establecer el valor del nombre del sujeto como -1 y limpiar el campo de edad
    document.getElementById("name_subject").value = "-1";
    document.getElementById("age_subject").value = "";
  }

  // Agregar un evento de escucha al cambio en el elemento select 'name_subject'
  document.getElementById("name_subject").addEventListener("change", function () {
    var initEvaluation = document.getElementById("startEvaluation");
    var selectedOption = this.value;
    // Verificar si se seleccionó una opción válida
    if (selectedOption != -1) {
      // Realizar una solicitud para filtrar datos basada en el procedimiento seleccionado
      fetch("filtrar_datos/?pid=" + encodeURIComponent(selectedOption))
        .then((response) => response.json())
        .then((data) => {
          console.log(data); // Imprime la respuesta obtenida del servidor

          // Obtener referencia al campo de edad del sujeto
          var ageSubject = document.getElementById("age_subject");
          // Iterar sobre las opciones del elemento select 'name_subject' para encontrar la opción seleccionada
          for (var i = 0; i < this.options.length; i++) {
            if (parseInt(this.options[i].value) === parseInt(data.proceeding[0].id)) {
              // Si se encuentra la opción seleccionada, establecerla como seleccionada, actualizar la edad del sujeto y habilitar el botón de inicio de la evaluación
              this.options[i].selected = true;
              ageSubject.value = calculateAge(data.proceeding[0].dateBirth);
              initEvaluation.classList.remove("disabled");
              break;
            }
          }
        })
        .catch((error) => console.error("Error:", error));
    } else {
      // Si no se seleccionó una opción válida, limpiar el campo de edad y deshabilitar el botón de inicio de la evaluación
      document.getElementById("age_subject").value = "";
      initEvaluation.classList.add("disabled");
    }
  });

  // Agregar un evento de escucha al cambio en el elemento select 'search_criteria'
  document.getElementById("search_criteria").addEventListener("change", function () {
    var search = document.getElementById("search_option");

    // Borrar opciones anteriores del elemento select 'search_option' y añadir una opción predeterminada
    search.innerHTML = "<option value=''>Seleccione opción</option>";

    // Verificar el criterio de búsqueda seleccionado y agregar opciones al elemento select 'search_option'
    if (this.value === "scholarship") {
      // Agregar opciones de escolaridad
      [
        "Ninguna",
        "Primaria",
        "Secundaria",
        "Bachillerato",
        "Universidad",
        "Maestría",
        "Doctorado",
        "Posdoctorado",
      ].forEach((scholarship) => {
        search.innerHTML += `<option value="${scholarship}">${scholarship}</option>`;
      });
    } else if (this.value === "gender") {
      // Agregar opciones de género
      ["Femenino", "Masculino"].forEach((gender) => {
        search.innerHTML += `<option value="${gender}">${gender}</option>`;
      });
    } else if (this.value === "todos") {
      // Agregar la opción 'Todos'
      search.innerHTML = "<option value='Todos'>Todos</option>";
    }
  });
});


// Función que filtra los procedimientos según el criterio de búsqueda seleccionado
function filterProceedings() {
  // Obtener los valores de los elementos HTML relevantes
  var criteria = document.getElementById("search_criteria").value;
  var filter = document.getElementById("search_option").value;
  var proceedings = document.getElementById("name_subject");
  var initEvaluation = document.getElementById("startEvaluation");

  // Verificar si los campos de criterio y filtro no están vacíos
  if (criteria != "" && filter != "") {
    // Evaluar el criterio seleccionado
    switch (criteria) {
      // Caso para filtrar por escolaridad o género
      case "scholarship":
      case "gender":
      case "todos":
        // Construir la URL de la solicitud fetch según el criterio seleccionado
        var url = "filtrar_datos/";
        if (criteria != "todos") url += "?" + criteria + "=" + encodeURIComponent(filter);

        // Realizar la solicitud fetch al servidor
        fetch(url)
          .then((response) => response.json())
          .then((data) => {
            // Imprimir la respuesta en la consola
            console.log(data);
            // Limpiar el campo de edad
            document.getElementById("age_subject").value = "";
            // Limpiar y actualizar el select con los nuevos datos de procedimientos
            proceedings.innerHTML = "";
            const selectEmpty = document.createElement("option");
            selectEmpty.value = "-1";
            selectEmpty.innerHTML = "Seleccione opción";
            proceedings.appendChild(selectEmpty);
            data.proceedings.forEach(function (proceeding) {
              var option = document.createElement("option");
              option.value = proceeding.id;
              option.text = proceeding.name;
              proceedings.appendChild(option);
            });
          })
          .catch((error) => console.error("Error:", error));

        // Deshabilitar el enlace de inicio de la evaluación
        initEvaluation.classList.add("disabled");
        break;
    }
  }
}

// Función que direcciona a la primera prueba que se aplicara
async function sendTest() {
  // Obtener elementos del DOM
  var banfe_id;
  var e = document.getElementById("startEvaluation"), // Enlace de inicio de evaluación
    t = document.getElementById("name_subject").value, // ID del sujeto
    n = document.getElementById("age_subject").value, // Edad del sujeto
    lista = []; // Lista de pruebas seleccionadas

  // Definir los datos a enviar en la solicitud POST
  const data = {
    pid: t,
    prueba: prueba
  }

  // Determinar la URL basada en el valor de la variable `prueba`
  let url;
  if (prueba === "cof") {
    url = "pruebasCOF_CPFM";
    data.prueba = "Orbitomedial";
  } else if (prueba === "cpfdl") {
    url = "pruebasCPFDL";
    data.prueba = "Dorsolateral";
  } else if (prueba === "cpfa") {
    url = "pruebasCPFA";
    data.prueba = "Prefrontal Anterior";
  } else {
    url = "pruebastotales";
    data.prueba = document.getElementById("test_to_aply").value;
  }

  console.log(data.prueba);
  // Enviar la solicitud POST
  try {
    const response = await sendPOST(url, data);

    // Aquí puedes manejar la respuesta del servidor
    console.log('Respuesta del servidor: ', response);

    // Por ejemplo, podrías redirigir a otra página solo si la respuesta indica éxito
    if (response.status === 'BANFE-2 Created Successfully') {
      console.log(response.status);
      console.log(response.banfe_id);
      banfe_id = response.banfe_id;
    } else {
      console.error('La respuesta del servidor indica un error');
      // Aquí podrías mostrar un mensaje de error al usuario o tomar otras acciones      
    }

    // Verificar qué tipo de prueba se está realizando
    if ("cof" === prueba || "cpfdl" === prueba) {
      // Lista de pruebas para cof o cpfdl
      if (parseInt(n) > 7) {
        lista = "cof" === prueba ? ["laberintos", "clasif_cartas-control", "stroopA-control", "cartas-control", "stroopB-control"] : ["laberintos", "senalamiento_autodirigido-control", "ordenamiento", "resta", "suma", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "torres-hanoi", "memoria_visoespacial-control"];
      } else {
        lista = "cof" === prueba ? ["laberintos", "clasif_cartas-control", "cartas-control"] : ["laberintos", "senalamiento_autodirigido-control", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "torres-hanoi"];
      }
      var r = encodeURIComponent(JSON.stringify(lista)); // Convertir la lista en una cadena codificada
      // Asignar el enlace con los parámetros correspondientes
      window.location.href = "laberintos?prueba=" + prueba + "&lista=" + r + "&num_prueba=" + 1 + "&pid=" + t + "&edad=" + n + "&banfe=" + banfe_id;
    } else if ("cpfa" === prueba) {
      // Lista de pruebas para cpfa
      if (parseInt(n) > 9) {
        lista = ["semanticas-control", "refranes-control", "metamemoria"];
      }else if(parseInt(n) > 7){
        lista = ["semanticas-control", "metamemoria"];
      } else {
        lista = ["metamemoria"];
      }
      var r = encodeURIComponent(JSON.stringify(lista)); // Convertir la lista en una cadena codificada
      // Asignar el enlace con los parámetros correspondientes 
      window.location.href = "semanticas-control?prueba=" + prueba + "&lista=" + r + "&num_prueba=" + 1 + "&pid=" + t + "&edad=" + n + "&banfe=" + banfe_id;
    } else {
      // Obtener lista de pruebas seleccionadas por el usuario
      lista = evaluateTest();
      // Verificar si hay pruebas seleccionadas
      lista.length != 0 ? (
        // Si hay pruebas seleccionadas, convertir la lista en una cadena codificada
        r = encodeURIComponent(JSON.stringify(lista)),
        // Asignar el enlace con los parámetros correspondientes
        window.location.href = lista[0] + "?prueba=" + prueba + "&lista=" + r + "&num_prueba=" + 1 + "&pid=" + t + "&edad=" + n + "&banfe=" + banfe_id
      ) : (
        // Si no hay pruebas seleccionadas, mostrar alerta
        mostrarModal("Debes seleccionar las pruebas a aplicar")
      )
    }

  } catch (error) {
    // Manejar errores que ocurran durante la solicitud POST
    alert('Error en la solicitud:', error);
    // Aquí puedes mostrar un mensaje de error al usuario o tomar otras acciones
  }

}

// Procedimiento para mostrar un modal con un mensaje y ejecutar una función al cerrarlo
function mostrarModal(mensaje, callback) {
  document.getElementById("text-modal-chron").textContent = mensaje;
  document.getElementById("box-modal-chron").style.width = "20%";
  document.getElementById("modal-chron").style.display = "block";
  document.getElementById("btnModal-chron").onclick = function () {
    document.getElementById("modal-chron").style.display = "none";
    if (callback) callback();
  };
}


// Función que evalúa qué pruebas ha seleccionado el aplicador
function evaluateTest() {
  // Definir un objeto con la edad mínima requerida para cada prueba
  const minimunAges = {
    "ordenamiento": 8,
    "resta": 8,
    "suma": 8,
    "stroopA-control": 8,
    "refranes-control": 10,
    "memoria_visoespacial-control": 8,
    "stroopB-control": 8
  };

  let age = document.getElementById("age_subject").value;

  // Crear un arreglo para almacenar las pruebas válidas
  let validTests = [];

  // Utilizando la función de filtro en un array de IDs de checkboxes,
  // se filtran los IDs de aquellos checkboxes que están marcados (checked)  
  let selectedTests = createTest();

  // Recorrer las pruebas seleccionadas
  for (let test of selectedTests) {
    // Verificar si la prueba tiene una edad mínima definida
    if (minimunAges.hasOwnProperty(test)) {
      // Verificar si la edad del sujeto es mayor o igual a la edad mínima requerida
      if (parseInt(age) >= minimunAges[test]) {
        // Agregar la prueba al arreglo de pruebas válidas
        validTests.push(test);
      }
    } else {
      // Si la prueba no tiene una edad mínima definida, agregarla al arreglo de pruebas válidas
      validTests.push(test);
    }
  }

  return validTests;
}


// Función para crear una lista de pruebas según el criterio seleccionado
function createTest() {
  let n = document.getElementById("age_subject").value; // Edad del sujeto
  // Inicializar la lista de pruebas
  let listTest = [];

  // Obtener el criterio seleccionado del elemento select
  let criteria = document.getElementById("test_to_aply").value;

  // Verificar el criterio seleccionado
  if (criteria != "") {
    // Caso: Todas las pruebas
    if (criteria === "allTests") {
      listTest = ["laberintos", "senalamiento_autodirigido-control", "ordenamiento", "resta", "suma", "clasif_cartas-control", "semanticas-control", "stroopA-control", "fluidez-verbal", "cartas-control", "refranes-control", "torres-hanoi", "metamemoria", "memoria_visoespacial-control", "stroopB-control"];
    }
    // Caso: Pruebas para CPFA y COF
    else if (criteria === "copfaTests") {
      if (parseInt(n) > 7) {
        if (parseInt(n) > 9) {
          listTest = ["laberintos", "clasif_cartas-control", "semanticas-control", "stroopA-control", "cartas-control", "refranes-control", "metamemoria", "stroopB-control"];
        } else {
          listTest = ["laberintos", "clasif_cartas-control", "semanticas-control", "stroopA-control", "cartas-control", "metamemoria", "stroopB-control"];
        }
      } else {
        listTest = ["laberintos", "clasif_cartas-control", "cartas-control", "metamemoria"];
      }
    }
    // Caso: Pruebas para COFDO
    else if (criteria === "cofdoTests") {
      // Lista de pruebas para cof o cpfdl
      if (parseInt(n) > 7) {
        listTest = ["laberintos", "senalamiento_autodirigido-control", "ordenamiento", "resta", "suma", "clasif_cartas-control", "semanticas-control", "stroopA-control", "fluidez-verbal", "cartas-control", "torres-hanoi", "memoria_visoespacial-control", "stroopB-control"];
      } else {
        listTest = ["laberintos", "senalamiento_autodirigido-control", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "cartas-control", "torres-hanoi"];
      }
    }
    // Caso: Otro criterio no especificado
    else {
      if (parseInt(n) > 7) {
        if (parseInt(n) > 9) {
          listTest = ["laberintos", "senalamiento_autodirigido-control", "ordenamiento", "resta", "suma", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "refranes-control", "torres-hanoi", "metamemoria", "memoria_visoespacial-control"];

        } else {
          listTest = ["laberintos", "senalamiento_autodirigido-control", "ordenamiento", "resta", "suma", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "torres-hanoi", "metamemoria", "memoria_visoespacial-control"];
        }
      } else {
        listTest = ["laberintos", "senalamiento_autodirigido-control", "clasif_cartas-control", "semanticas-control", "fluidez-verbal", "torres-hanoi", "metamemoria"];
      }
    }
  }

  // Retornar la lista de pruebas creada
  return listTest;
}

async function sendPOST(url, data) {
  // Función para obtener el token CSRF de la cookie
  function getCSRFToken() {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      .split('=')[1];
    return cookieValue;
  }

  // Obtener el token CSRF
  const csrfToken = getCSRFToken();

  // Hacer la solicitud POST incluyendo el token CSRF
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(data)
    });
    if (!response.ok) {
      // Si la respuesta del servidor indica un error, lanzar un error
      throw new Error('Error en la solicitud: ' + response.statusText);
    } else {
      console.log("estamos dentro")
    }
    return await response.json();
  } catch (error) {
    // Manejar el error aquí
    console.error('Error:', error);
    // Puedes lanzar el error nuevamente para que sea manejado en la llamada a esta función
    throw error;
  }
}
