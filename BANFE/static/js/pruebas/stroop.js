let values = new Array(83);
let stroopErrors = 0;
let nonStroopErrors = 0;
let currentTest;
let stroopTimerActive = false;
let correctAnswers = 0;

let stroopClickSound = document.querySelector(".figure-sound");

window.completeStroop = false;


// Procedimiento que inicia la prueba del lado del sujeto
function startStroopTest(testType) {
  const modalText = document.getElementById("text-modal-stroop");

  if (testType === "A") {
    modalText.textContent = "Ahora, lo que tiene que hacer es leer en voz alta cada palabra, columna por columna, iniciando en la columnas superiores y continuando con las columnas de abajo. Cuando vea una palabra subrayada, tiene que mencionar el color con el que esa palabra está pintada y no lo que está escrito. ¿Está preparado? Comience.";
  } else {
    modalText.textContent = "A continuación, leerá en voz alta cada palabra, columna por columna. Iniciará con las columnas de la parte superior y luego con las columnass de abajo. Cuando yo diga 'leer' en una columna, usted deberá leer cada palabra de la columna, pero cuando le diga 'color', debe mencionar en toda esa columna el color con el que están escritas las palabras, y así iremos alternando cada columna hasta terminar la prueba. ¿Preparado? Comience.";
  }

  showStroopModal();
}

// Procedimiento que ayuda a mostrar el modal e iniciar el reloj
function showStroopModal() {
  document.getElementById("box-modal-stroop").style.width = "40%";
  document.getElementById("modal-stroop").style.display = "block";
  document.getElementById("btnModal-stroop").onclick = function () {
    stroopClickSound.play();
    document.getElementById("modal-stroop").style.display = "none";
    if (
      document.getElementById("text-modal-stroop").textContent !=
      "Prueba finalizada"
    ) {
      startStroopTimer();
    } else {
      alert("eee")
    }
  }
}

// Procedimiento para iniciar el reloj Stroop
function startStroopTimer() {
  stroopTimerActive = setInterval(updateStroopTimer, 10)
}

// Procedimiento que incrementa los aciertos
function countCorrect(position) {
  stroopClickSound.play();
  adjustScores(position);
  correctAnswers++;
  values[position - 1] = "acierto";
}

// Procedimiento que incrementa los errores
function countErrors(type, position) {
  stroopClickSound.play();
  adjustScores(position);

  if (type === "stroop") {
    stroopErrors++;
  } else {
    nonStroopErrors++;
  }

  values[position - 1] = type;
}

// Procedimiento que decrementa los errores o aciertos si ya fueron seleccionados
function adjustScores(position) {
  if (values[position - 1] === "stroop") {
    stroopErrors--;
  } else if(values[position - 1] === "nostroop") {
    nonStroopErrors--;
  } else if (values[position - 1] === "acierto") {
    correctAnswers--;
  }
}

// Procedimiento que los contadores e inhabilita la tabla
function resetStroopTest() {
  correctAnswers = 0;
  stroopErrors = 0;
  nonStroopErrors = 0;

  values.fill(null);
  enableTable(currentTest, true);
}


// Procedimiento que muestra los datos de BANFE actualizados
function displayStroopResults(testType) {
  if (testType === "A") {
    document.getElementById("aciertos_stroop").textContent = correctAnswers;
    document.getElementById("err_stroop").textContent = stroopErrors;
    document.getElementById("errno_stroop").textContent = nonStroopErrors;
  
    if (document.getElementById("segundos_stroop").textContent === "300") {
      enableTable(testType, true);
    }
  } else {
    document.getElementById("aciertos_stroop-B").textContent = correctAnswers;
    document.getElementById("err_stroop-B").textContent = stroopErrors;
    document.getElementById("errno_stroop-B").textContent = nonStroopErrors;

    if (document.getElementById("segundos_stroop-b").textContent === "300") {
      enableTable(testType, true);
    }
  }
}

// Procedimiento que habilita e inhabilita la tabla
function enableTable(testType, enable) {
  currentTest = testType;
  const totalButtons = 85;

  for (let i = 1; i < totalButtons; i++) {
    const stroopBtn = document.getElementById(`btn-stroop-${i}`);
    const nonStroopBtn = document.getElementById(`btn-nostroop-${i}`);
    const correctBtn = document.getElementById(`btn-acierto-${i}`);

    if (testType === "A" && isStroopPositionA(i)) {
      stroopBtn.disabled = enable;
    } else if (testType !== "A" && isStroopPositionB(i)) {
      stroopBtn.disabled = enable;
    } else {
      nonStroopBtn.disabled = enable;
    }
    correctBtn.disabled = enable;
  }

  window.completeStroop = enable;
}

// Procedimiento que identifica las posiciones en Stroop A
function isStroopPositionA(position) {
  const stroopPositionsA = [3, 6, 8, 10, 12, 19, 21, 23, 26, 28, 30, 37, 38, 40, 42, 43, 45, 48, 50, 52, 53, 55, 57, 59, 67, 70, 72, 79, 81, 83, 84];
  return stroopPositionsA.includes(position);
}

// Procedimiento que identifica las posiciones en Stroop B
function isStroopPositionB(position) {
  return (
    (position > 6 && position < 13) ||
    (position > 18 && position < 25) ||
    (position > 30 && position < 37) ||
    (position > 42 && position < 49) ||
    (position > 54 && position < 61) ||
    (position > 66 && position < 73) ||
    (position > 78 && position < 85)
  );
}

let stroopSeconds = 0;
let stroopMilliseconds = 0;

// Procedimiento que funciona como cronometro para el sujeto
function updateStroopTimer() {
  if (stroopSeconds === 300) {
    clearInterval(stroopTimerActive);
    window.completeStroop = true;

    document.getElementById("text-modal-stroop").textContent = "Prueba finalizada";
    document.getElementById("box-modal-stroop").style.width = "20%";
    document.getElementById("modal-stroop").style.display = "block";    
  }

  if (stroopMilliseconds < 99) {
    stroopMilliseconds++;
  }

  if (stroopMilliseconds === 99) {
    stroopMilliseconds = -1;
    stroopSeconds++;
  }
}