// Definición de variables
var alarm = document.querySelector(".alarm_sound"),
  clickMaze = document.querySelector(".click-sound"),
  startMaze = false,
  pauseMaze = false,
  mazes = 0,
  startTime = 0,
  timerControl,
  totalMazes = 5;  // Número total de laberintos

// Función para iniciar cada uno de los laberintos
function startMazes() {
  clickMaze.play(); // Reproduce el sonido de clic

  if (startMaze) {
    // Si la prueba fue pausada, continúa
    if (pauseMaze) {
      timerControl = setInterval(mazeTimer, 10);
      startTime = seconds;
      pauseMaze = false;
      enableMazeButtons(mazes + 1);
    }
  } else {
    // Si es la primera vez que se inicia la prueba
    timerControl = setInterval(mazeTimer, 10);
    startTime = seconds;
    document.getElementById("reset_mazes").disabled = false;
    startMaze = true;
    enableMazeButtons(1);
    document.getElementById("finish-1").disabled = false;
  }
}


// Función que detiene el tiempo de cada laberinto
function stopMazes() {
  clickMaze.play();
  pauseMaze = true;
  clearInterval(timerControl);
  mazes++;

  // Actualiza el promedio y el tiempo del laberinto actual
  updateAverage();
  updateMazeTime();

  // Deshabilita botones del laberinto actual y habilita el siguiente si queda
  disableMazeButtons(mazes);
  if (mazes < totalMazes) {
    enableMazeButtons(mazes + 1);
  } else {
    document.getElementById("reset_mazes").disabled = true;
  }
}

// Función para reiniciar toda la prueba
function resetMazes() {
  clickMaze.play();
  clearInterval(timerControl);
  centiseconds = seconds = 0;
  startMaze = false;
  mazes = 0;

  // Reinicia la UI
  resetUI();
  disableMazeButtons(mazes);
  document.getElementById("reset_mazes").disabled = true;
  document.getElementById("finish-1").disabled = true;
}

// Función que actúa como cronómetro
function mazeTimer() {
  let ageTime = (parseInt(age) < 8) ? 300 : 240;

  if (seconds === ageTime) {  // Si se llega al tiempo máximo permitido
    alarm.play();
    stopMazes();
    showCompletionModal();
  }

  centiseconds = (centiseconds + 1) % 100;
  if (centiseconds === 0) seconds++;

  document.getElementById("secondsP1").textContent = seconds;

  if (mazes > 0) {
    updateAverage();
  }
}


// Función para sumar errores en un laberinto
function incrementError(maze, error) {
  clickMaze.play();
  updateErrors(maze, error, 1);
}


// Función para restar errores en un laberinto
function decrementError(maze, error) {
  if (document.getElementById(`${error}-${maze}`).textContent != 0) {
    clickMaze.play();
    updateErrors(maze, error, -1);
  }
}

// Función para actualizar errores totales y por laberinto
function updateErrors(maze, error, delta) {
  document.getElementById(`${error}-${maze}`).textContent =
    parseInt(document.getElementById(`${error}-${maze}`).textContent, 10) + delta;

  let totalError = `total-${error}`;
  document.getElementById(totalError).textContent =
    parseInt(document.getElementById(totalError).textContent, 10) + delta;
}

// Función que habilita los botones del laberinto correspondiente
function enableMazeButtons(maze) {
  disableMazeButtons(); // Inhabilita todos los botones primero

  // Habilita los botones del laberinto actual
  document.getElementById(`start_${maze}`).disabled = false;
  document.getElementById(`finish-${maze}`).disabled = false;

  ["touch", "cross", "trap"].forEach(error => {
    document.getElementById(`dec-${error}-${maze}`).disabled = false;
    document.getElementById(`inc-${error}-${maze}`).disabled = false;
  });
}

// Función que inhabilita todos los botones de los laberintos
function disableMazeButtons() {
  for (let i = 1; i <= totalMazes; i++) {
    document.getElementById(`start_${i}`).disabled = true;
    document.getElementById(`finish-${i}`).disabled = true;

    ["touch", "cross", "trap"].forEach(error => {
      document.getElementById(`dec-${error}-${i}`).disabled = true;
      document.getElementById(`inc-${error}-${i}`).disabled = true;
    });
  }
}

// Función que actualiza el promedio del tiempo de los laberintos
function updateAverage() {
  if (mazes > 0) {
    document.getElementById("average").textContent =
      Math.round(parseInt(document.getElementById("secondsP1").textContent) / mazes);
  } else {
    document.getElementById("average").textContent = "0";
  }
}

// Función que muestra el modal de finalización
function showCompletionModal() {
  document.getElementById("modal-text-mazes").textContent = "Test completed";
  document.getElementById("modal-box-mazes").style.width = "20%";
  document.getElementById("modal-mazes").style.display = "block";

  document.getElementById("modal-btn-mazes").onclick = function () {
    clickMaze.play();
    document.getElementById("modal-mazes").style.display = "none";
  };
}

// Función para resetear la interfaz de usuario
function resetUI() {
  document.getElementById("secondsP1").textContent = "0";
  document.getElementById("average").textContent = "0";

  for (let i = 1; i <= totalMazes; i++) {
    ["touch", "cross", "trap"].forEach(error => {
      document.getElementById(`${error}-${i}`).textContent = "0";
    });
    document.getElementById(`time-${i}`).textContent = "0";
  }

  ["total-touch", "total-cross", "total-trap"].forEach(total => {
    document.getElementById(total).textContent = "0";
  });
}