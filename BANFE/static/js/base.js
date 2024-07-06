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
  alert("Función iniciada");
  alert("ID: " + banfe);

  let url = lista[test - 1];
  alert("URL obtenida: " + url);

  let results = getResults(url);
  alert("Resultados obtenidos: " + results);
  const data = {
    pid: pid,
    banfe: banfe,
    result: results,
  };

  alert("Datos creados: " + JSON.stringify(data));

  // Enviar la solicitud POST
  try {
    alert("hola antes del POST");
    const response = await sendPOST(url, data);
    alert("hola: " + response);

    // Aquí puedes manejar la respuesta del servidor
    alert("Respuesta del servidor: ", response);

    // Por ejemplo, podrías redirigir a otra página solo si la respuesta indica éxito
    if (response.status === "Subtest Created Successfully") {
      banfe_id = response.banfe_id;

      // Verificar si la lista está vacía
      alert("LISTA: "+lista)
      if (lista.length !== 0) {
        // Obtiene el índice del último elemento de la lista
        let lastIndex = lista.length - 1;
        // Convertir test a entero
        test = parseInt(test);
        alert("No vacia: " + lista);

        // Verificar si test es mayor que el último índice de la lista
        alert(test + " es mayor a: " + lastIndex);
        if (test > lastIndex) {
          // Establecer el enlace al inicio si test es mayor que el último índice de la lista
          if (lista[test - 1] === "ordenamiento") {
            alert(lista[test - 1]);
            window.location.href = "../";
          } else {
            alert(lista[test - 1]);
            window.location.href = "./";
          }
        } else {
          alert(test + " es menor a: " + lastIndex);
          alert("No vacia: " + lista);

          // Codificar lista en un componente URI
          listaEncoded = encodeURIComponent(JSON.stringify(lista));
          // Construir el enlace con la próxima prueba
          if (lista[test - 1] === "ordenamiento") {
            if (lista[test] === "resta") {
              alert(lista[test - 1]);
              alert(lista[test]);
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
              alert(lista[test - 1]);
              alert(lista[test]);
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
              alert(lista[test - 1]);
              alert(lista[test]);
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
              alert(lista[test - 1]);
              alert(lista[test]);
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
        alert(window.location.href);
      }
    } else {
      console.error("La respuesta del servidor indica un error");
      alert("Hubo un error: " + response);
      // Aquí podrías mostrar un mensaje de error al usuario o tomar otras acciones
    }
  } catch (error) {
    // Manejar errores que ocurran durante la solicitud POST
    console.error("Error en la solicitud:", error);
    alert("Hubo un error: " + response);
    // Aquí puedes mostrar un mensaje de error al usuario o tomar otras acciones
  }
}

function getResults(test) {
  let result = [];
  alert("TEST: " + test);
  switch (test) {
    case "laberintos":
      alert("TEST 1: " + test);
      result = [
        document.getElementById("total-toca").textContent,
        document.getElementById("total-atraviesa").textContent,
        document.getElementById("total-atrapado").textContent,
        document.getElementById("segundosP1").textContent,
      ];
      alert("RESULT: " + result);
      break;
    case "senalamiento_autodirigido-control":
      result = [
        document.getElementById("successeSignaling").textContent,
        document.getElementById("perseverationSignaling").textContent,
        document.getElementById("omissionSignaling").textContent,
        document.getElementById("secondSignaling").textContent,
      ];
      alert(result);
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
      alert(result);
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
      alert("estoy en semanticas");
      result = [
        document.getElementById("total-concretas").textContent,
        document.getElementById("total-funcionales").textContent,
        document.getElementById("total-abstractas").textContent,
        document.getElementById("total-cat").textContent,
        document.getElementById("total-prom").textContent,
        document.getElementById("puntos-finales").textContent,
      ];
      alert("guardado");
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
      alert("TEST 1: " + test);
      alert(
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
      alert("RESULT: " + result);
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
  alert("RETORNAMOS: " + result);
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
    alert("TOKEN: "+csrfToken);
    if (!response.ok) {
      alert("Error en la solicitud: " + response.statusText);
      // Si la respuesta del servidor indica un error, lanzar un error
      throw new Error("Error en la solicitud: " + response.statusText);
    } else {
      alert("estamos dentro");
      alert("Respuesta correcta: " + response.statusText);
    }
    return await response.json();
  } catch (error) {
    // Manejar el error aquí
    console.error("Error:", error);
    alert("Error en la solicitud: " + error.message); // Muestra el mensaje de error
    // Puedes lanzar el error nuevamente para que sea manejado en la llamada a esta función
    throw error;
  }
}
