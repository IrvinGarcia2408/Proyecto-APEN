let click_cronometro = document.querySelector(".figure-sound");
let alarmChronometer = document.querySelector(".alarm_chronometer");
let centesimas = 0;
let segundos = 0;

window.completeSemantics = false;

// Variables para almacenar los identificadores de los elementos DOM
let time, init, stopped, reset, watch;
var control;

// Función para iniciar el cronómetro
function start(t, s, i, p, r) {
  click_cronometro.play();
  // Iniciar el intervalo para actualizar el cronómetro
  control = setInterval(chronometer, 10);
  // Asignar valores a las variables globales
  time = t;
  init = i;
  stopped = p;
  reset = r;
  watch = s;
  // Desactivar el botón de inicio y habilitar los botones de parada y reinicio
  document.getElementById(init).disabled = true;
  document.getElementById(stopped).disabled = false;
  document.getElementById(reset).disabled = false;
}

// Función para detener el cronómetro
function stoped() {
  clearInterval(control);
  // Deshabilitar los botones de parada y reinicio
  document.getElementById(stopped).disabled = true;
  document.getElementById(reset).disabled = true;
}

// Función para reiniciar el cronómetro
function restart() {
  click_cronometro.play();
  clearInterval(control);
  // Reiniciar las variables de tiempo y centésimas
  centesimas = segundos = 0;
  // Actualizar la visualización del cronómetro
  document.getElementById(watch).innerHTML = "0";
  // Habilitar el botón de inicio y deshabilitar los botones de parada y reinicio
  document.getElementById(init).disabled = false;
  document.getElementById(stopped).disabled = true;
  document.getElementById(reset).disabled = true;
}

// Función para actualizar el cronómetro
function chronometer() {
  // Si los segundos alcanzan el límite establecido
  if (segundos == time) {
    // Reproducir alarma
    alarmChronometer.play();
    clearInterval(control);
    // Mostrar mensaje de finalización de la prueba
    document.getElementById(stopped).disabled = true;
    document.getElementById(reset).disabled = true;
    document.getElementById("text-modal-chron").textContent = "Prueba finalizada";
    document.getElementById("box-modal-chron").style.width = "20%";
    document.getElementById("modal-chron").style.display = "block";
    // Asignar acción al botón del modal
    document.getElementById("btnModal-chron").onclick = function () {
      click_cronometro.play();
      document.getElementById("modal-chron").style.display = "none";
    };
  }
  // Incrementar las centésimas y actualizar la visualización del cronómetro
  if (centesimas < 99) {
    centesimas++;
  }
  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
    document.getElementById(watch).innerHTML = "" + segundos;
  }
}
