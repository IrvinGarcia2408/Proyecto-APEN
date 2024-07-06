// Selección de elementos de audio para los efectos de sonido
var click_cartas = document.querySelector(".figure-sound");
var castigo_0 = document.querySelector(".castigo-0_sound");
var castigo_2 = document.querySelector(".castigo-2_sound");
var castigo_3 = document.querySelector(".castigo-3_sound");
var castigo_5 = document.querySelector(".castigo-5_sound");
var castigo_8 = document.querySelector(".castigo-8_sound");
var castigo_12 = document.querySelector(".castigo-12_sound");

// Definición de variables para las cartas y los castigos
var cartas = [1, 1, 1, 1, 1];

var castigos = [
  [0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],
  [0, 0, 0, -3, 0, 0, 0, -3, 0, 0, 0, -3, 0, 0, 0, -3, 0, 0],
  [0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5],
  [0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8],
  [0, -12, 0, -12, -12, 0, -12, 0, -12, -12, 0, -12, 0, -12, -12, 0, -12, 0],
];

// Variable que indica si la carta está activa o no
let card_active = false;

// Variables de control adicionales
var mensaje = false;
var parada = false;

// Función que inicia la prueba de cartas para el sujeto
function iniciarCartas() {
  // Mostrar mensaje inicial con instrucciones
  document.getElementById("text-modal-cartas").textContent =
    "El objetivo de esta tarea es lograr la mayor cantidad posible de puntos. Para esto, puede escoger cartas con valor desde uno hasta cinco puntos, en el orden que usted quiera. Cada vez que tome una carta de cualquier grupo, yo tomaré la carta que le corresponde del grupo de enfrente, las cuales pueden o no contener castigos. Si la carta de castigo contiene el número '0', conservará los puntos obtenidos; si por ejemplo la carta tiene '-2', usted perderá esos puntos.";
  document.getElementById("box-modal-cartas").style.width = "40%";
  document.getElementById("modal-cartas").style.display = "block";

  // Manejador de evento para el botón modal
  document.getElementById("btnModal-cartas").onclick = function () {
    // Reproducir sonido de clic
    click_cartas.play();
    // Ocultar el modal
    document.getElementById("modal-cartas").style.display = "none";
    // Iniciar temporizador si no está activo
    if (!card_active) {
      temporizador_cartas = setInterval(relojCartas, 10);
      card_active = true;
    }
  };
}

// Procedimiento que procesa la toma de una carta
function tomarCarta(torre) {
  // Verificar si la carta está disponible y la prueba está activa
  if (cartas[torre - 1] <= 18 && card_active) {
    // Bloquear las cartas temporalmente
    bloquearCartas(true);
    // Reproducir sonido de clic
    click_cartas.play();
    // Resaltar el borde de la carta seleccionada
    document.getElementById("puntos-" + torre).style.border = "5px solid #9e2";

    // Verificar si es el último valor de la carta
    if (cartas[torre - 1] == 18) {
      // Si es el último valor, limpiar la carta y mostrar el castigo
      document.getElementById("pila-" + torre).textContent = "";
      document.getElementById("pila-" + torre).classList.remove("cartas-puntos");
      setTimeout(() => {
        document.getElementById("castigos-" + torre).textContent = castigos[torre - 1][cartas[torre - 1] - 2];
        restarPuntos(castigos[torre - 1][cartas[torre - 1] - 2]);
        document.getElementById("menos-" + torre).classList.remove("cartas-castigos");
        document.getElementById("pila-" + torre).textContent = "";
        document.getElementById("castigos-" + torre).style.border = "5px solid #d12";
      }, "1200");
    } else {
      // Si no es el último valor, mostrar el valor de la carta y el castigo
      document.getElementById("puntos-" + torre).className = "cartas-puntos";
      document.getElementById("puntos-" + torre).textContent = torre;
      setTimeout(() => {
        restarPuntos(castigos[torre - 1][cartas[torre - 1] - 2]);
        document.getElementById("castigos-" + torre).className = "cartas-castigos";
        document.getElementById("castigos-" + torre).textContent = castigos[torre - 1][cartas[torre - 1] - 2];
        document.getElementById("castigos-" + torre).style.border = "5px solid #d12";
      }, "1200");
    }

    // Restablecer el borde de la carta después de un tiempo
    setTimeout(() => {
      document.getElementById("puntos-" + torre).style.border = "none";
    }, "1000");

    // Restablecer el borde del castigo después de un tiempo y desbloquear las cartas
    setTimeout(() => {
      document.getElementById("castigos-" + torre).style.border = "none";
      bloquearCartas(false);
    }, "2000");

    // Incrementar el contador de cartas y enviar los datos al servidor
    cartas[torre - 1]++;
    DjangoPOST("./" + torre, [torre, castigos[torre - 1][cartas[torre - 1] - 2]]);
  }
}

// Procedimiento que reproduce el sonido de castigos correspondiente
function restarPuntos(puntos) {
  // Reproducir el sonido según el valor de los puntos
  switch (puntos) {
    case 0:
      castigo_0.play(); // Reproducir sonido de castigo 0
      break;
    case -2:
      castigo_2.play(); // Reproducir sonido de castigo -2
      break;
    case -3:
      castigo_3.play(); // Reproducir sonido de castigo -3
      break;
    case -5:
      castigo_5.play(); // Reproducir sonido de castigo -5
      break;
    case -8:
      castigo_8.play(); // Reproducir sonido de castigo -8
      break;
    case -12:
      castigo_12.play(); // Reproducir sonido de castigo -12
      break;
  }
}

// Procedimiento que bloquea las cartas
function bloquearCartas(estado) {
  // Verificar el estado y agregar o quitar la clase "cartas-apagadas" según corresponda
  if (estado) {
    // Bloquear las cartas
    document.getElementById("pila-1").classList.add("cartas-apagadas");
    document.getElementById("pila-2").classList.add("cartas-apagadas");
    document.getElementById("pila-3").classList.add("cartas-apagadas");
    document.getElementById("pila-4").classList.add("cartas-apagadas");
    document.getElementById("pila-5").classList.add("cartas-apagadas");
  } else {
    // Desbloquear las cartas
    document.getElementById("pila-1").classList.remove("cartas-apagadas");
    document.getElementById("pila-2").classList.remove("cartas-apagadas");
    document.getElementById("pila-3").classList.remove("cartas-apagadas");
    document.getElementById("pila-4").classList.remove("cartas-apagadas");
    document.getElementById("pila-5").classList.remove("cartas-apagadas");
  }
}

let total = 0; // Variable para almacenar el tiempo total
let segundos_cartas = 0;
let centesimas_cartas = 0;


// Procedimiento que funciona como cronómetro para el sujeto
function relojCartas() {
  // Comprobar si el tiempo total alcanza un valor específico
  if (total == 90 || segundos_cartas == 298) {
    // Si se alcanza el tiempo límite, detener el temporizador y realizar acciones finales
    setTimeout(() => {
      clearInterval(temporizador_cartas);
      DjangoPOST("./finalizado/" + 1, 1); // Enviar señal de finalización al servidor
      // Mostrar mensaje de prueba finalizada en un modal
      document.getElementById("text-modal-cartas").textContent = "Prueba finalizada";
      document.getElementById("box-modal-cartas").style.width = "20%";
      document.getElementById("modal-cartas").style.display = "block";
    }, 2000);
  }

  // Incrementar las centésimas de segundo y actualizar los segundos si es necesario
  if (centesimas_cartas < 99) {
    centesimas_cartas++;
  }
  if (centesimas_cartas == 99) {
    centesimas_cartas = -1;
  }
  if (centesimas_cartas == 0) {
    segundos_cartas++;
    console.log(segundos_cartas);
    // Calcular el tiempo total sumando los valores de las cartas seleccionadas
    total =
      (cartas[0] - 1) +
      (cartas[1] - 1) +
      (cartas[2] - 1) +
      (cartas[3] - 1) +
      (cartas[4] - 1);
  }
}
// Procedimiento que muestra el mensaje de finalizado
function imprimirMensaje() {
  // Mostrar el mensaje de prueba finalizada en un modal
  document.getElementById("text-modal-cartas").textContent = "Prueba finalizada";
  document.getElementById("box-modal-cartas").style.width = "20%";
  document.getElementById("modal-cartas").style.display = "block";

  // Configurar el evento click para el botón de cerrar modal
  document.getElementById("btnModal-cartas").onclick = function () {
    click_cartas.play(); // Reproducir sonido de clic
    document.getElementById("modal-cartas").style.display = "none"; // Ocultar el modal
    mensaje = true; // Establecer mensaje como mostrado
  };
}

/* Funciones generales */

// Función para realizar una solicitud POST a través de Django
function DjangoPOST(url, datos) {
  const csrftoken = getCookie("csrftoken"); // Obtener el token CSRF

  // Realizar la solicitud POST utilizando fetch API
  fetch(url, {
    method: "POST",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(datos),
  })
    .then((response) => {
      console.log(response); // Mostrar la respuesta en la consola
    })
    .catch((error) => {
      console.log(error); // Manejar errores de la solicitud
    });
}

// Función asincrónica para realizar una solicitud GET a través de Django
async function DjangoGET(url) {
  let response = await fetch(url); // Realizar la solicitud GET utilizando fetch API
  const data = await response.json(); // Convertir la respuesta a formato JSON

  return data; // Devolver los datos obtenidos
}

// Función para obtener el valor de una cookie por su nombre
function getCookie(name) {
  let cookieValue = null; // Inicializar el valor de la cookie como nulo
  if (document.cookie && document.cookie !== "") {
    // Verificar si existen cookies y no están vacías
    const cookies = document.cookie.split(";"); // Separar las cookies por punto y coma
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim(); // Eliminar los espacios en blanco alrededor de la cookie
      // ¿La cadena de cookie comienza con el nombre de la cookie que estamos buscando?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        // Decodificar y asignar el valor de la cookie
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break; // Salir del bucle
      }
    }
  }
  return cookieValue; // Devolver el valor de la cookie encontrada o nulo si no se encuentra
}