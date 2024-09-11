let click_ordenamiento = document.querySelector(".figure-sound");
var ensayo = 1;
let posicion = 1;

// Procedimiento que anota la palabra seleccionada dentro de la página
function writeWord(lista, fila, palabra) {
  click_ordenamiento.play(); // Reproducir sonido de ordenamiento

  // Verificar si la celda está vacía antes de escribir la posición
  if (document.getElementById("list-" + lista + "_en-" + ensayo + "_ord-" + fila).textContent == "") {
    // Si está vacía, escribir la posición
    document.getElementById("list-" + lista + "_en-" + ensayo + "_ord-" + fila).textContent = posicion;
    DjangoPOST("./ordenamiento/" + palabra, [palabra, posicion, lista]); // Enviar información a través de una solicitud POST a Django
    console.log("entramos"); // Mostrar mensaje de depuración en la consola
  } else {
    // Si no está vacía, simplemente enviar información a través de una solicitud POST a Django
    DjangoPOST("./ordenamiento/" + palabra, [palabra, posicion, lista]);
  }
  posicion++; // Incrementar la posición para la siguiente palabra
}

// Procedimiento que apunta la intrusión dada
function writeIntrusion(lista) {
  // Verificar si se presionó la tecla Enter
  if (event.key == "Enter") {
    // Obtener el valor del campo de texto
    var palabra = document.getElementById("textin-" + lista).value;
    // Verificar si el campo de texto tiene contenido
    if (palabra.length > 0) {
      // Enviar la palabra al servidor a través de una solicitud POST a Django
      DjangoPOST("./ordenamiento/" + palabra, [palabra, posicion, lista]);
      // Limpiar el campo de texto después de enviar la palabra
      document.getElementById("textin-" + lista).value = "";
      // Actualizar el elemento de la lista de intrusiones con la palabra añadida
      if (document.getElementById("list-in-" + lista + "_" + ensayo).textContent != "") {
        // Si ya hay contenido en la lista de intrusiones, agregar la nueva palabra al final
        document.getElementById("list-in-" + lista + "_" + ensayo).textContent += ", " + palabra.toLowerCase() + " (" + posicion + ")";
      } else {
        // Si la lista de intrusiones está vacía, establecer la nueva palabra como primer elemento
        document.getElementById("list-in-" + lista + "_" + ensayo).textContent = palabra.toLowerCase() + " (" + posicion + ")";
      }
      // Incrementar la posición para la siguiente palabra
      posicion++;
    } else {
      // Mostrar un mensaje en un modal si el campo de texto está vacío
      document.getElementById("text-modal-ord").textContent = "Campo vacío";
      document.getElementById("box-modal-ord").style.width = "20%";
      document.getElementById("modal-ord").style.display = "block";
    }
  }
}

// Procedimiento que verifica si el ensayo es correcto
async function checkList(lista) {
  click_ordenamiento.play();
  resultado = await DjangoGET("./ordenamiento/validar/" + lista, lista);
  if (resultado.estado === 0) {
    correctEssay(lista);
  } else {
    incorrectEssay(lista);
  }
}

// Procedimiento para manejar un ensayo correcto
function correctEssay(lista) {
  $("#state-" + lista + "-" + ensayo).load(" #state-" + lista + "-" + ensayo);
  ensayo = 1;
  posicion = 1;
  console.log(lista)
  if (lista < 3) {
    if(lista === 2 && (parseInt(age) < 10 || ((parseInt(age) > 30 && parseInt(age) < 56) && (school > 3 && school < 10)))){
      showModal("Prueba finalizada");
      turnOffButtons(lista+1);
    }else{
      showModal("Siguiente lista");
    }
  } else {
    showModal("Prueba finalizada");
  }
  turnOffButtons(lista);
}

// Procedimiento para manejar un ensayo incorrecto
function incorrectEssay(lista) {
  $("#state-" + lista + "-" + ensayo).load(" #state-" + lista + "-" + ensayo);

  if (ensayo === 5) {
    if (lista < 3) {
      if(lista === 2 && (parseInt(age) < 10 || ((parseInt(age) > 30 && parseInt(age) < 56) && (school > 3 && school < 10)))){
        showModal("Prueba finalizada");
        turnOffButtons(lista+1);
      }else{
        ensayo = 1;
        posicion = 1;
        showModal("Siguiente lista");
      }
    } else {
      showModal("Prueba finalizada");
    }
    turnOffButtons(lista);
  } else {
    posicion = 1;
    ensayo++;
    showModal("Siguiente ensayo");
  }

}


// Procedimiento para mostrar un modal con un mensaje dado
function showModal(mensaje) {
  document.getElementById("text-modal-ord").textContent = mensaje;
  document.getElementById("box-modal-ord").style.width = "20%";
  document.getElementById("modal-ord").style.display = "block";
}

// Configurar evento para cerrar el modal al hacer clic en el botón
document.getElementById("btnModal-ord").onclick = function () {
  click_ordenamiento.play();
  document.getElementById("modal-ord").style.display = "none";
};

// Procedimiento que inhabilta los botones
function turnOffButtons(lista) {
  switch (lista) {
    case 1:
      document.getElementById("btn-1_1").classList.add("botones-apagados");
      document.getElementById("btn-1_2").classList.add("botones-apagados");
      document.getElementById("btn-1_3").classList.add("botones-apagados");
      document.getElementById("btn-1_4").classList.add("botones-apagados");
      document.getElementById("btn-1_5").classList.add("botones-apagados");
      document.getElementById("textin-1").classList.add("botones-apagados");
      document.getElementById("sigensayo-1").classList.add("botones-apagados");
      break;
    case 2:
      document.getElementById("btn-2_1").classList.add("botones-apagados");
      document.getElementById("btn-2_2").classList.add("botones-apagados");
      document.getElementById("btn-2_3").classList.add("botones-apagados");
      document.getElementById("btn-2_4").classList.add("botones-apagados");
      document.getElementById("btn-2_5").classList.add("botones-apagados");
      document.getElementById("btn-2_6").classList.add("botones-apagados");
      document.getElementById("textin-2").classList.add("botones-apagados");
      document.getElementById("sigensayo-2").classList.add("botones-apagados");
      break;
    case 3:
      document.getElementById("btn-3_1").classList.add("botones-apagados");
      document.getElementById("btn-3_2").classList.add("botones-apagados");
      document.getElementById("btn-3_3").classList.add("botones-apagados");
      document.getElementById("btn-3_4").classList.add("botones-apagados");
      document.getElementById("btn-3_5").classList.add("botones-apagados");
      document.getElementById("btn-3_6").classList.add("botones-apagados");
      document.getElementById("btn-3_7").classList.add("botones-apagados");
      document.getElementById("textin-3").classList.add("botones-apagados");
      document.getElementById("sigensayo-3").classList.add("botones-apagados");
      break;
  }
}

// Procedimiento que reinicia la prueba
function restartSorting() {
  DjangoPOST("./ordenamiento/reiniciar/" + 1, 1);
  setTimeout(location.reload(), 2000);
}

/*  Funciones generales  */
function DjangoPOST(url, datos) {
  const csrftoken = getCookie("csrftoken");

  fetch(url, {
    method: "POST",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(datos),
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
}

async function DjangoGET(url) {
  let response = await fetch(url);
  const data = await response.json();

  return data;
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
