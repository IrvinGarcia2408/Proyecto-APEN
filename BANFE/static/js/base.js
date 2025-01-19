// Selecciona los elementos del DOM
var navSesion = document.querySelector(".navbar__sesion");
var navMenu = document.querySelector(".navbar__menu");

var modal = document.getElementById("modalIncompleteTest");
// Asignar referencia al botón de cerrar dentro del modal
var modalCloseButton = document.getElementById("modalCloseButton");



// Agrega un event listener para alternar una clase al hacer clic en navSesion
navSesion.addEventListener("click", () => {
  navMenu.classList.toggle("navbar_observe");
});

// Función que limpia la lista que se recibe del servidor
function cleanList(list) {
  // Eliminar los códigos HTML escapados y reemplazarlos por comillas simples
  var notScape = list.replace(/&#x27;/g, "'");

  // Eliminar los corchetes al principio y al final de la cadena
  var notBrackets = notScape.slice(1, -1);

  // Eliminar las comillas simples alrededor de cada elemento de la lista
  var notQuotationMarks = notBrackets.replace(/'/g, "");

  // Dividir la cadena en una lista usando la coma y el espacio como separadores
  var lista = notQuotationMarks.split(", ");

  return lista; // Devolver la lista limpia
}

document.addEventListener("DOMContentLoaded", function () {
  // Obtener la URL actual de la página
  const currentPath = window.location.pathname;

  // Buscar todos los enlaces en el menú
  const menuLinks = document.querySelectorAll('.menu a');

  // Recorrer cada enlace
  menuLinks.forEach(link => {
    // Comparar el href del enlace con la URL actual
    if (link.getAttribute('href') === currentPath) {
      // Si coincide, agregar la clase 'active' al div padre
      link.parentElement.classList.add('active');
    }
  });
});


function getResults(test) {
  let result = [];

  console.log("TEST: "+test);

  switch (test) {
    case 'laberintos':
      result = getLabyrinthResults();
      break;
    case "senalamiento_autodirigido-control":
      result = getSignalingResults();
      break;
    case "ordenamiento":
      result = getSortingResults();
      break;
    case "resta":
      result = getSubstractionResults();
      break;
    case "suma":
      result = getAdditionResults();
      break;
    case "clasif_cartas-control":
      result = getCardSortingResults();
      break;
    case "semanticas-control":
      result = getSemanticResults();
      break;
    case "stroopA-control":
      result = getStroopAResults();
      break;
    case "fluidez-verbal":
      result = getVerbalFluencyResults();
      break;
    case "cartas-control":
      result = getCardGameResults();
      break;
    case "refranes-control":
      result = getSayingResults();
      break;
    case "torres-hanoi":
      result = getTowersHanoiResults();
      break;
    case "metamemoria":
      result = getMetamemoryResults();
      break;
    case "memoria_visoespacial-control":
      result = getVisuospatialMemoryResults();
      break;
    case "stroopB-control":
      result = getStroopBResults();
      break;
  }

  return result;
}

function getLabyrinthResults() {
  return [
    document.getElementById("total-touch").textContent,
    document.getElementById("total-cross").textContent,
    document.getElementById("total-caught").textContent,
    document.getElementById("seconds_labyrinths").textContent,
  ];  
}

function getSignalingResults() {
  return [
    document.getElementById("successeSignaling").textContent,
    document.getElementById("perseverationSignaling").textContent,
    document.getElementById("omissionSignaling").textContent,
    document.getElementById("secondSignaling").textContent,
  ];
}

function getSortingResults() {
  if (
    parseInt(age) < 9 ||
    (parseInt(age) > 30 &&
      parseInt(age) < 56 &&
      parseInt(school) > 3 &&
      parseInt(school) < 10)
  ) {
    return [
      document.getElementById("num_ensayo_list1").textContent,
      document.getElementById("error_orden_list1").textContent,
      document.getElementById("perseveraciones_list1").textContent,
      document.getElementById("instrusiones_list1").textContent,

      document.getElementById("num_ensayo_list2").textContent,
      document.getElementById("error_orden_list2").textContent,
      document.getElementById("perseveraciones_list2").textContent,
      document.getElementById("instrusiones_list2").textContent,
    ];
  } else {
    return [
      document.getElementById("num_ensayo_list1").textContent,
      document.getElementById("error_orden_list1").textContent,
      document.getElementById("perseveraciones_list1").textContent,
      document.getElementById("instrusiones_list1").textContent,

      document.getElementById("num_ensayo_list2").textContent,
      document.getElementById("error_orden_list2").textContent,
      document.getElementById("perseveraciones_list2").textContent,
      document.getElementById("instrusiones_list2").textContent,

      document.getElementById("num_ensayo_list3").textContent,
      document.getElementById("error_orden_list3").textContent,
      document.getElementById("perseveraciones_list3").textContent,
      document.getElementById("instrusiones_list3").textContent,
    ];
  }
}

function getSubstractionResults() {
  if (parseInt(age) > 9) {
    return [
      document.getElementById("aciertos-resta-1").textContent,
      document.getElementById("errores-resta-1").textContent,
      document.getElementById("segundos_resta_1").textContent,

      document.getElementById("aciertos-resta-2").textContent,
      document.getElementById("errores-resta-2").textContent,
      document.getElementById("segundos_resta_2").textContent,
    ];
  } else {
    return [
      document.getElementById("aciertos-resta-1").textContent,
      document.getElementById("errores-resta-1").textContent,
      document.getElementById("segundos_resta_1").textContent,
    ];
  }  
}

function getAdditionResults() {
  return [
    document.getElementById("aciertos-suma").textContent,
    document.getElementById("errores-suma").textContent,
    document.getElementById("segundos_suma").textContent,
  ];
}

function getCardSortingResults() {
  return [
    document.getElementById("aciertos_cards_sorting").textContent,
    document.getElementById("errores_cards_sorting").textContent,
    document.getElementById("perseveraciones_cards_sorting").textContent,
    document.getElementById("err-mto_cards_sorting").textContent,
    document.getElementById("pers-dif_cards_sorting").textContent,
    document.getElementById("segundos").textContent,
  ];
}

function getSemanticResults() {
  return [
    document.getElementById("total-concretas").textContent,
    document.getElementById("total-funcionales").textContent,
    document.getElementById("total-abstractas").textContent,
    document.getElementById("total-cat").textContent,
    document.getElementById("total-prom").textContent,
    document.getElementById("puntos-finales").textContent,
  ];
}

function getStroopAResults() {
  return [
    document.getElementById("aciertos_stroop").textContent,
    document.getElementById("err_stroop").textContent,
    document.getElementById("errno_stroop").textContent,
    document.getElementById("segundos_stroop").textContent,
  ];
}

function getVerbalFluencyResults() {
  return [
    document.getElementById("aciertos_fluidez").textContent,
    document.getElementById("perseveraciones_fluidez").textContent,
    document.getElementById("intrusiones_fluidez").textContent,
  ];
}

function getCardGameResults() {
  return [
    document.getElementById("total_score_cards").textContent,
    document.getElementById("percentege_risk").textContent,
    document.getElementById("question_one").value,
    document.getElementById("question_two").value,
    document.getElementById("question_three").value,
    document.getElementById("question_four").value,
  ];
}

function getSayingResults() {
  return [
    document.getElementById("refranes-resultados").textContent,
    document.getElementById("segundos_refranes").textContent,
  ];
}

function getTowersHanoiResults() {
  if (parseInt(age) > 9) {
    return [
      document.getElementById("mov-torre-1").textContent,
      document.getElementById("segundos_torres-1").textContent,
      document.getElementById("err_1-1").textContent,
      document.getElementById("err_2-1").textContent,
      document.getElementById("err_total-1").textContent,
      document.getElementById("mov-torre-2").textContent,
      document.getElementById("segundos_torres-2").textContent,
      document.getElementById("err_1-2").textContent,
      document.getElementById("err_2-2").textContent,
      document.getElementById("err_total-2").textContent,
    ];
  } else {
    return [
      document.getElementById("mov-torre-1").textContent,
      document.getElementById("segundos_torres-1").textContent,
      document.getElementById("err_1-1").textContent,
      document.getElementById("err_2-1").textContent,
      document.getElementById("err_total-1").textContent,
    ];
  }
}

function getMetamemoryResults() {
  return [
    document.getElementById("intrusion_metamemoria").textContent,
    document.getElementById("perseveracion_metamemoria").textContent,
    document.getElementById("err-positivo_metamemoria").textContent,
    document.getElementById("err-negativo_metamemoria").textContent,
    document.getElementById("err-total_metamemoria").textContent,
  ];
}

function getVisuospatialMemoryResults() {
  return [
    document.getElementById("err-ord").textContent,
    document.getElementById("err-sust").textContent,
    document.getElementById("persev").textContent,
    document.getElementById("sec-max").textContent,
  ];
}

function getStroopBResults() {
  return [
    document.getElementById("aciertos_stroop-B").textContent,
    document.getElementById("err_stroop-B").textContent,
    document.getElementById("errno_stroop-B").textContent,
    document.getElementById("segundos_stroop-b").textContent,
  ];
}

// Función que verifica si la prueba ha sido completada
function isTestComplete(test) {
  let isComplete = false;
  console.log("Z: "+test)

  switch (test) {
    case "laberintos":
      isComplete = window.completeMazes;
      break;
    case "senalamiento_autodirigido-control":
      isComplete = window.completeSignaling;
      break;      
    case "ordenamiento":
      isComplete = window.completeSorting;
      break;
    case "resta":
      isComplete = window.completeSubstraction;
      break;      
    case "suma":
      isComplete = window.completeAddition;
      break;            
    case "clasif_cartas-control":
      isComplete = window.completeCardSorting;
      break;
    case "semanticas-control":
      isComplete = true;
      break;      
    case "stroopA-control":
      isComplete = window.completeStroop;
      break;
    case "fluidez-verbal":
      isComplete = true;
      break;
    case "cartas-control":
      isComplete = window.completeCardGame;
      break;
    case "refranes-control":
      isComplete = window.completeSayings;
      break;
    case "torres-hanoi":
      isComplete = window.completeTowers;
      break;  
    case "metamemoria":
      isComplete = window.completeMetamemory;
      break;  
    case "memoria_visoespacial-control":
      isComplete = true;
      break;        
    case "stroopB-control":
      isComplete = window.completeStroop;
      break;
      
      // Checar mejor que en vez del test, consigamos el nombre y ya comparamos el nombre de la prueba
  }
  console.log("Completado: "+isComplete);

  return isComplete;
}

async function nextTest() {
  try {
    
    console.log("Función iniciada");
    let url = lista[test -1];

    //  Verificar si la prueba fue completada usando el número de prueba
    if (!isTestComplete(lista[test - 1])) {
      //  Si la prueba no fue completada, mostrar el modal
      modal.style.display = "block";
      return; //  Salir de la función, no pasar a la siguiente prueba
    }

    console.log("Avanzamos");

    // Si la prueba fue completada, continuar con la lógica normal
    let results = getResults(url);

    const data = createData(pid, banfe, results);
    const response = await sendPOST(url, data)

    handleResponse(response);
  } catch (error) {
    console.error("Error en la solicitud: ", error);
  }
}

// Función que se ejecuta cuando el usuario cierra el modal
modalCloseButton.addEventListener('click', function() {
  modal.style.display = "none";  // Cerrar el modal
});

function createData(pid, banfe, results) {
  return {
    pid: pid,
    banfe: banfe,
    result: results
  };
}

function handleResponse(response) {
  if (response.status === "Test Created Successfully") {
    banfe_id = response.banfe_id;

    if (lista.length !== 0) {
      let lastIndex = lista.length - 1;
      test = parseInt(test);
      console.log("Lista no vacía: "+lista);

      if (test > lastIndex) {
        redirectHome();
      } else {
        redirectToNextTest();
      }
    }
  } else {
    console.error("La respuesta del servidor indica un error: ", response);
    console.log("Hubo un error: "+JSON.stringify(response));
  }
}

function redirectHome(){
  if (lista[test - 1] === "ordenamiento") {
    window.location.href = "../";
  } else {
    window.location.href = "./";
  }
}

function redirectToNextTest() {
  let listEncoded = encodeURIComponent(JSON.stringify(lista));

  if (lista[test - 1] === "ordenamiento") {
    if (lista[test] === "resta") {
      redirectToSpecificTest(lista[test], listEncoded, true);
    } else {
      redirectToSpecificTest(lista[test], listEncoded, false);
    }
  } else {
    if (lista[test - 1] === "ordenamiento") {
      redirectToBanfeTest(lista[test], listEncoded);
    } else {
      redirectToSpecificTest(lista[test], listEncoded, true);
    }
  }
}

function redirectToSpecificTest(testName, listEncoded, isSameLevel) {
  let basePath = isSameLevel ? "" : "../";
  console.log(lista[test - 1]);
  console.log(testName);

  window.location.href =
    basePath +
    testName +
    "?lista=" +
    listEncoded +
    "&num_prueba=" +
    (test + 1) +
    "&pid=" +
    pid +
    "&edad=" +
    age +
    "&banfe=" +
    banfe_id;
}

function redirectToBanfeTest(testName, listaEncoded) {
  console.log(lista[test - 1]);
  console.log(testName);

  window.location.href =
    "banfe/" +
    testName +
    "?lista=" +
    listaEncoded +
    "&num_prueba=" +
    (test + 1) +
    "&pid=" +
    pid +
    "&edad=" +
    age +
    "&banfe=" +
    banfe_id;
}


async function sendPOST(url, data) {
  const csrfToken = getCSRFToken();

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      return await response.json();
    } else {
      throw new Error("Error en la solicitud POST: " + response.statusText);
    }
  } catch (error) {
    console.error("Error:", error);
    throw error;
  }
}

function getCSRFToken() {
  const cookieValue = document.cookie
    .split("; ")
    .find((row) => row.startsWith("csrftoken="))
    ?.split("=")[1];
  return cookieValue;
}