// Selecciona los elementos del DOM
var navSesion = document.querySelector(".navbar__sesion");
var navMenu = document.querySelector(".navbar__menu");

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

async function nextTest() {
  try {
    console.log("Función iniciada");
    console.log("ID: " + banfe);

    let url = lista[test - 1];
    console.log("URL obtenida: " + url);

    let results = getResults(url);
    console.log("Resultados obtenidos: " + results);

    const data = {
      pid: pid,
      banfe: banfe,
      result: results,
    };

    console.log("Datos creados: " + JSON.stringify(data));

    console.log("Antes de enviar POST");
    const response = await sendPOST(url, data);
    console.log("Respuesta recibida");

    console.log("Respuesta del servidor: ", response);

    if (response.status === "Subtest Created Successfully") {
      banfe_id = response.banfe_id;

      if (lista.length !== 0) {
        let lastIndex = lista.length - 1;
        test = parseInt(test);
        console.log("No vacia: " + lista);

        if (test > lastIndex) {
          if (lista[test - 1] === "ordenamiento") {
            console.log(lista[test - 1]);
            window.location.href = "../";
          } else {
            console.log(lista[test - 1]);
            window.location.href = "./";
          }
        } else {
          listaEncoded = encodeURIComponent(JSON.stringify(lista));
          if (lista[test - 1] === "ordenamiento") {
            if (lista[test] === "resta") {
              console.log(lista[test - 1]);
              console.log(lista[test]);
              window.location.href =
                lista[test] +
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
            } else {
              console.log(lista[test - 1]);
              console.log(lista[test]);
              window.location.href =
                "../" +
                lista[test] +
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
          } else {
            if (lista[test - 1] === "ordenamiento") {
              console.log(lista[test - 1]);
              console.log(lista[test]);
              window.location.href =
                "banfe/" +
                lista[test] +
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
            } else {
              console.log(lista[test - 1]);
              console.log(lista[test]);
              window.location.href =
                lista[test] +
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
          }
        }
        console.log("Redirigiendo a: " + window.location.href);
      }
    } else {
      console.error("La respuesta del servidor indica un error: ", response);
      console.log("Hubo un error: " + JSON.stringify(response));
    }
  } catch (error) {
    console.error("Error en la solicitud:", error);
    console.log("Hubo un error durante la solicitud: " + error.message);
  }
}

function getResults(test) {
  let result = [];
  console.log("TEST: " + test);
  switch (test) {
    case "laberintos":
      console.log("TEST 1: " + test);
      result = [
        document.getElementById("total-toca").textContent,
        document.getElementById("total-atraviesa").textContent,
        document.getElementById("total-atrapado").textContent,
        document.getElementById("segundosP1").textContent,
      ];
      console.log("RESULT: " + result);
      break;
    case "senalamiento_autodirigido-control":
      result = [
        document.getElementById("successeSignaling").textContent,
        document.getElementById("perseverationSignaling").textContent,
        document.getElementById("omissionSignaling").textContent,
        document.getElementById("secondSignaling").textContent,
      ];
      console.log(result);
      break;
    case "ordenamiento":
      if (
        parseInt(age) < 9 ||
        (parseInt(age) > 30 &&
          parseInt(age) < 56 &&
          parseInt(school) > 3 &&
          parseInt(school) < 10)
      ) {
        result = [
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
        result = [
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

      break;
    case "resta":
      if (parseInt(age) > 9) {
        result = [
          document.getElementById("aciertos-resta-1").textContent,
          document.getElementById("errores-resta-1").textContent,
          document.getElementById("segundos_resta_1").textContent,

          document.getElementById("aciertos-resta-2").textContent,
          document.getElementById("errores-resta-2").textContent,
          document.getElementById("segundos_resta_2").textContent,
        ];
      } else {
        result = [
          document.getElementById("aciertos-resta-1").textContent,
          document.getElementById("errores-resta-1").textContent,
          document.getElementById("segundos_resta_1").textContent,
        ];
      }
      console.log(result);
      break;
    case "suma":
      result = [
        document.getElementById("aciertos-suma").textContent,
        document.getElementById("errores-suma").textContent,
        document.getElementById("segundos_suma").textContent,
      ];
      break;
    case "clasif_cartas-control":
      result = [
        document.getElementById("aciertos_cards_sorting").textContent,
        document.getElementById("errores_cards_sorting").textContent,
        document.getElementById("perseveraciones_cards_sorting").textContent,
        document.getElementById("err-mto_cards_sorting").textContent,
        document.getElementById("pers-dif_cards_sorting").textContent,
        document.getElementById("segundos").textContent,
      ];
      break;
    case "semanticas-control":
      console.log("estoy en semanticas");
      result = [
        document.getElementById("total-concretas").textContent,
        document.getElementById("total-funcionales").textContent,
        document.getElementById("total-abstractas").textContent,
        document.getElementById("total-cat").textContent,
        document.getElementById("total-prom").textContent,
        document.getElementById("puntos-finales").textContent,
      ];
      console.log("guardado");
      break;
    case "stroopA-control":
      result = [
        document.getElementById("aciertos_stroop").textContent,
        document.getElementById("err_stroop").textContent,
        document.getElementById("errno_stroop").textContent,
        document.getElementById("segundos_stroop").textContent,
      ];
      break;
    case "fluidez-verbal":
      result = [
        document.getElementById("aciertos_fluidez").textContent,
        document.getElementById("perseveraciones_fluidez").textContent,
        document.getElementById("intrusiones_fluidez").textContent,
      ];
      break;
    case "cartas-control":
      console.log("TEST 1: " + test);
      console.log(
        "TEST X: " + document.getElementById("percentege_risk").textContent
      );
      result = [
        document.getElementById("total_score_cards").textContent,
        document.getElementById("percentege_risk").textContent,
        document.getElementById("question_one").value,
        document.getElementById("question_two").value,
        document.getElementById("question_three").value,
        document.getElementById("question_four").value,
      ];
      console.log("RESULT: " + result);
      break;
    case "refranes-control":
      result = [
        document.getElementById("refranes-resultados").textContent,
        document.getElementById("segundos_refranes").textContent,
      ];
      break;
    case "torres-hanoi":
      if (parseInt(age) > 9) {
        result = [
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
        result = [
          document.getElementById("mov-torre-1").textContent,
          document.getElementById("segundos_torres-1").textContent,
          document.getElementById("err_1-1").textContent,
          document.getElementById("err_2-1").textContent,
          document.getElementById("err_total-1").textContent,
        ];
      }
      break;
    case "metamemoria":
      result = [
        document.getElementById("intrusion_metamemoria").textContent,
        document.getElementById("perseveracion_metamemoria").textContent,
        document.getElementById("err-positivo_metamemoria").textContent,
        document.getElementById("err-negativo_metamemoria").textContent,
        document.getElementById("err-total_metamemoria").textContent,
      ];
      break;
    case "memoria_visoespacial-control":
      result = [
        document.getElementById("err-ord").textContent,
        document.getElementById("err-sust").textContent,
        document.getElementById("persev").textContent,
        document.getElementById("sec-max").textContent,
      ];
      break;
    case "stroopB-control":
      result = [
        document.getElementById("aciertos_stroop-B").textContent,
        document.getElementById("err_stroop-B").textContent,
        document.getElementById("errno_stroop-B").textContent,
        document.getElementById("segundos_stroop-b").textContent,
      ];
      break;
  }
  console.log("RETORNAMOS: " + result);
  return result;
}

async function sendPOST(url, data) {
  // Función para obtener el token CSRF de la cookie
  function getCSRFToken() {
    const cookieValue = document.cookie
      .split("; ")
      .find((row) => row.startsWith("csrftoken="))
      ?.split("=")[1];
    return cookieValue;
  }

  // Obtener el token CSRF
  const csrfToken = getCSRFToken();

  // Hacer la solicitud POST incluyendo el token CSRF
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(data),
    });
    console.log("TOKEN: "+csrfToken);
    if (response.ok) {
      console.log("estamos dentro");
      console.log("Respuesta correcta: " + response.statusText);
    }
    return await response.json();
  } catch (error) {
    // Manejar el error aquí
    console.error("Error:", error);
    console.log("Error en la solicitud: " + error.message); // Muestra el mensaje de error
    // Puedes lanzar el error nuevamente para que sea manejado en la llamada a esta función
    throw error;
  }
}
