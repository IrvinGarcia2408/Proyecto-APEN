// Selección de elementos de audio para los efectos de sonido
const clickCardsSound = document.querySelector(".figure-sound");
const cardSound = document.querySelector(".card_sound");
const alarmSubject = document.querySelector(".alarm_sound-subject");
const alarmControl = document.querySelector(".alarm_sound-subject");

const penalty0Sound = document.querySelector(".penalty-0_sound");
const penalty2Sound = document.querySelector(".penalty-2_sound");
const penalty3Sound = document.querySelector(".penalty-3_sound");
const penalty5Sound = document.querySelector(".penalty-5_sound");
const penalty8Sound = document.querySelector(".penalty-8_sound");
const penalty12Sound = document.querySelector(".penalty-12_sound");

// Definición de variables para las cartas y los castigos
const cards = [1, 1, 1, 1, 1];

const penalties = [
  [0, 0, 0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],
  [0, 0, 0, -3, 0, 0, 0, -3, 0, 0, 0, -3, 0, 0, 0, -3, 0, 0],
  [0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5, 0, 0, -5],
  [0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8, 0, -8],
  [0, -12, 0, -12, -12, 0, -12, 0, -12, -12, 0, -12, 0, -12, -12, 0, -12, 0]
];

// Variable que indica si la carta está activa o no
let isCardActive = false;


// Variables de control adicionales
let isMessageShown = false;
let isPaused = false;

let total = 0; // Variable para almacenar el tiempo total
let cards_seconds = 0;
let cards_centiseconds = 0;
let timer;

window.completeCardGame = false;


// Función que inicia la prueba de cartas para el sujeto
function startCardTest() {
  showModal("El objetivo de esta tarea es lograr la mayor cantidad posible de puntos. Para esto, puede escoger cartas con valor desde uno hasta cinco puntos, en el orden que usted quiera. Cada vez que tome una carta de cualquier grupo, yo tomaré la carta que le corresponde del grupo de enfrente, las cuales pueden o no contener castigos. Si la carta de castigo contiene el número '0', conservará los puntos obtenidos; si por ejemplo la carta tiene '-2', usted perderá esos puntos.", "35%");

  // Manejador de evento para el botón modal
  document.getElementById("btnModal-cartas").onclick = function () {
    clickCardsSound.play();
    hideModal();

    // Iniciar temporizador si no está activo
    if (!isCardActive) {
      timer = setInterval(runCardTimer, 10);
      isCardActive = true;
      window.completeCardGame = false;
    }
  } 
}


// Procedimiento que procesa la toma de una carta
function drawCard(tower) {
  // Verificar si la carta está disponible y la prueba está activa
  if (cards[tower - 1] <= 18 && isCardActive){
    // Bloquear las cartas temporalmente
    lockCards(true);
    cardSound.play();

    // Resaltar el borde de la carta seleccionada
    highlightCard(tower);

    // Verificar si es el último valor de la carta
    if (cards[tower - 1] === 18) {
      processLastCard(tower);
    } else {
      processRegularCard(tower);
    }

    // Restablecer el borde de la carta después de un tiempo
    resetCardHighlight(tower, 1000);
    resetPenaltyHighlight(tower, 2000);

    // Incrementar el contador de cartas y enviar los datos al servidor
    cards[tower - 1]++;
    DjangoPOST("./" + tower, [tower, penalties[tower - 1][cards[tower - 1] - 2]]);

  }
}

// Procedimiento que procesa la última carta en una torre
function processLastCard(tower) {
  document.getElementById("pile-" + tower).textContent = "";
  document.getElementById("pile-" + tower).classList.remove("cartas-puntos");
  setTimeout(() => {
      document.getElementById("penalties-" + tower).textContent = penalties[tower - 1][cards[tower - 1] - 2];
      applyPenalty(penalties[tower - 1][cards[tower - 1] - 2]);
      document.getElementById("penalty-" + tower).classList.remove("cartas-castigos");
      document.getElementById("pile-" + tower).textContent = "";
      document.getElementById("penalties-" + tower).style.border = "5px solid #d12";
  }, 1200);
}

// Procedimiento que procesa una carta regular en una torre
function processRegularCard(tower) {
  document.getElementById("points-" + tower).className = "cartas-puntos";
  document.getElementById("points-" + tower).textContent = tower;
  setTimeout(() => {
      applyPenalty(penalties[tower - 1][cards[tower - 1] - 2]);
      document.getElementById("penalties-" + tower).className = "cartas-castigos";
      document.getElementById("penalties-" + tower).textContent = penalties[tower - 1][cards[tower - 1] - 2];
      document.getElementById("penalties-" + tower).style.border = "5px solid #d12";
  }, 1200);
}


// Procedimiento que reproduce el sonido de castigos correspondiente
function applyPenalty(points) {
  // Reproducir el sonido según el valor de los puntos
  switch (points) {
    case 0:
      penalty0Sound.play(); // Reproducir sonido de castigo 0
      break;
    case -2:
      penalty2Sound.play(); // Reproducir sonido de castigo -2
      break;
    case -3:
      penalty3Sound.play(); // Reproducir sonido de castigo -3
      break;
    case -5:
      penalty5Sound.play(); // Reproducir sonido de castigo -5
      break;
    case -8:
      penalty8Sound.play(); // Reproducir sonido de castigo -8
      break;
    case -12:
      penalty12Sound.play(); // Reproducir sonido de castigo -12
      break;
  }
}

// Procedimiento que bloquea y desbloquea las cartas
function lockCards(state) {
  const action = state ? 'add' : 'remove';

  for (let i = 1; i <= 5; i++) {
    document.getElementById("pile-" + i).classList[action]("cartas-apagadas");
  }
}

// Procedimiento para resaltar la tarjeta seleccionada
function highlightCard(tower) {
  document.getElementById("points-" + tower).style.border = "5px solid #9e2";
}

// Función para restablecer el resaltado de la tarjeta después de un retraso
function resetCardHighlight(tower, delay) {
  setTimeout(() => {
      document.getElementById("points-" + tower).style.border = "none";
  }, delay);
}

// Función para restablecer el resaltado de penalización después de un retraso
function resetPenaltyHighlight(tower, delay) {
  setTimeout(() => {
      document.getElementById("penalties-" + tower).style.border = "none";
      lockCards(false);
  }, delay);
}

// Procedimiento que funciona como cronómetro para el sujeto
function runCardTimer() {
  if (total === 90 || cards_seconds === 298) {
    stopCardTimer();
    lockCards(true);
  }

  if (cards_centiseconds < 99) {
    cards_centiseconds++;
  } else {
    cards_centiseconds = 0;
    cards_seconds++;
    total = cards.reduce((acc, card) => acc + (card - 1), 0);
  }
}

// Función para detener el temporizador de la tarjeta y finalizar la prueba
function stopCardTimer() {
  alarmSubject.play();
  window.completeCardGame = true;
  setTimeout(() => {
    clearInterval(timer);
    DjangoPOST("./finalizado/1", 1);
    showModal("Prueba finalizada", "20%");
    // Manejador de evento para el botón modal
    document.getElementById("btnModal-cartas").onclick = function () {
      clickCardsSound.play();
      hideModal();
      isMessageShown = true;
    } 
  }, 2000);
}

// Funciones de utilidad para la gestión modal
function showModal(message, width) {
  document.getElementById("text-modal-cartas").textContent = message;
  document.getElementById("box-modal-cartas").style.width = width;
  document.getElementById("modal-cartas").style.display = "block";
}

function hideModal() {
  document.getElementById("modal-cartas").style.display = "none";
}

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