let valores = new Array(83);
let err_stroop = 0;
let err_nostroop = 0;
let prueba;
let reloj_stroop = false;

let click_stroop = document.querySelector(".figure-sound");

// Procedimiento que inicia la prueba del lado del sujeto
function iniciarStroop(prueba) {
  if (prueba == "A") {
    document.getElementById("text-modal-stroop").textContent = "Ahora, lo que tiene que hacer es leer en voz alta cada palabra, columna por columna, iniciando en la columnas superiores y continuando con las columnas de abajo. Cuando vea una palabra subrayada, tiene que mencionar el color con el que esa palabra está pintada y no lo que está escrito. ¿Está preparado? Comience.";
  } else {
    document.getElementById("text-modal-stroop").textContent = "A continuación, leerá en voz alta cada palabra, columna por columna. Iniciará con las columnas de la parte superior y luego con las columnass de abajo. Cuando yo diga 'leer' en una columna, usted deberá leer cada palabra de la columna, pero cuando le diga 'color', debe mencionar en toda esa columna el color con el que están escritas las palabras, y así iremos alternando cada columna hasta terminar la prueba. ¿Preparado? Comience.";
  }

  document.getElementById("box-modal-stroop").style.width = "40%";
  document.getElementById("modal-stroop").style.display = "block";
  document.getElementById("btnModal-stroop").onclick = function () {
    click_stroop.play();
    document.getElementById("modal-stroop").style.display = "none";
    if (
      document.getElementById("text-modal-stroop").textContent !=
      "Prueba finalizada"
    ) {
      control = setInterval(relojStroop, 10);
    }
  };
}

// Procedimiento que incrementa los aciertos
function contarAciertos(posicion) {
  click_stroop.play();
  buscarPuntos(posicion);
  aciertos++;
  valores[posicion - 1] = "acierto";
}

// Procedimiento que incrementa los errores
function contarErrores(tipo, posicion) {
  click_stroop.play();
  buscarPuntos(posicion);
  if (tipo == "stroop") {
    err_stroop++;
  } else {
    err_nostroop++;
  }
  valores[posicion - 1] = tipo;
}

// Procedimiento que decrementa los errores o aciertos si ya fueron seleccionados
function buscarPuntos(posicion) {
  if (valores[posicion - 1] == "stroop") {
    err_stroop--;
  } else if (valores[posicion - 1] == "nostroop") {
    err_nostroop--;
  } else if (valores[posicion - 1] == "acierto") {
    aciertos--;
  }
}

// Procedimiento que los contadores e inhabilita la tabla
function limpiarStroop() {
  aciertos = 0;
  err_stroop = 0;
  err_nostroop = 0;

  while (valores.length > 0) {
    valores.pop();
  }
  habilitarTabla(prueba, true);
}

// Procedimiento que muestra los datos de BANFE actualizados
function mostrarStroop(prueba) {
  console.log("mostrado")
  if (prueba == "A") {
    document.getElementById("aciertos_stroop").textContent = aciertos;
    document.getElementById("err_stroop").textContent = err_stroop;
    document.getElementById("errno_stroop").textContent = err_nostroop;

    if (document.getElementById("segundos_stroop").textContent == 300) {
      habilitarTabla(prueba, true);
    }
  } else {
    document.getElementById("aciertos_stroop-B").textContent = aciertos;
    document.getElementById("err_stroop-B").textContent = err_stroop;
    document.getElementById("errno_stroop-B").textContent = err_nostroop;

    console.log(document.getElementById("segundos_stroop-b").textContent);

    if (document.getElementById("segundos_stroop-b").textContent == 300) {
      habilitarTabla(prueba, true);
    }
  }
}

// Procedimiento que habilita e inhabilita la tabla
function habilitarTabla(tabla, valor) {
  prueba = tabla;
  if (tabla == "A") {
    for (let i = 1; i < 85; i++) {
      if (
        i == 3 ||
        i == 6 ||
        i == 8 ||
        i == 10 ||
        i == 12 ||
        i == 19 ||
        i == 21 ||
        i == 23 ||
        i == 26 ||
        i == 28 ||
        i == 30 ||
        i == 37 ||
        i == 38 ||
        i == 40 ||
        i == 42 ||
        i == 43 ||
        i == 45 ||
        i == 48 ||
        i == 50 ||
        i == 52 ||
        i == 53 ||
        i == 55 ||
        i == 57 ||
        i == 59 ||
        i == 67 ||
        i == 70 ||
        i == 72 ||
        i == 79 ||
        i == 81 ||
        i == 83 ||
        i == 84
      ) {
        document.getElementById("btn-stroop-" + i).disabled = valor;
      } else {
        document.getElementById("btn-nostroop-" + i).disabled = valor;
      }
      document.getElementById("btn-acierto-" + i).disabled = valor;
    }
  } else {
    console.log(tabla);
    for (let i = 1; i < 85; i++) {
      if (
        (i > 6 && i < 13) ||
        (i > 18 && i < 25) ||
        (i > 30 && i < 37) ||
        (i > 42 && i < 49) ||
        (i > 54 && i < 61) ||
        (i > 66 && i < 73) ||
        (i > 78 && i < 85)
      ) {
        document.getElementById("btn-stroop-" + i).disabled = valor;
        console.log("X: " + i);
      } else {
        console.log(i);
        document.getElementById("btn-nostroop-" + i).disabled = valor;
      }
      document.getElementById("btn-acierto-" + i).disabled = valor;
    }
  }
}

let secStroopA = 0;
let cenStroopA = 0;
// Procedimiento que funciona como cronometro para el sujeto
function relojStroop() {
  if (secStroopA == 300) {
    clearInterval(control);
    document.getElementById("text-modal-stroop").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-stroop").style.width = "20%";
    document.getElementById("modal-stroop").style.display = "block";
  }
  console.log("Segundos: " + secStroopA + " | Centesimas: " + cenStroopA);
  if (cenStroopA < 99) {
    cenStroopA++;
  }

  if (cenStroopA == 99) {
    cenStroopA = -1;
  }
  if (cenStroopA == 0) {
    secStroopA++;
  }
}
