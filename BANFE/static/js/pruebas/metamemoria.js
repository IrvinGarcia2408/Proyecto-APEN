let click_metamemoria = document.querySelector(".figure-sound");

let total_palabras = 0;

window.completeMetamemory = false;

// Variables utilizadas por BANFE
let meta_intru = 0;
let meta_persev = 0;
let meta_errpos = 0;
let meta_errneg = 0;

let palabras = [
  "pera",
  "tubo",
  "vaca",
  "bote",
  "goma",
  "lija",
  "mano",
  "arco",
  "carta",
];
let palabras_instruidas = new Array(20);

// Procedimiento que recibe la predicción de palabras aprendidas por el sujeto
function anotarPredictor() {
  if (event.key == "Enter") {
    let numero = document.getElementById("predictor").value;
    if (numero.length > 0) {
      document.getElementById("predictor").value = "";
      document.getElementById("predictor_valor-" + ensayo).textContent = numero;
      iniciarPanel(false);
      document.getElementById("reiniciar_metamemoria").disabled = false;
    } else {
      document.getElementById("text-modal-ord").textContent = "Campo vacío";
      document.getElementById("box-modal-ord").style.width = "20%";
      document.getElementById("modal-ord").style.display = "block";
    }
  }
}

// Procedimiento que apunta la intrusión dada
function apuntarIntrusion() {
  if (event.key == "Enter") {
    let palabra = document.getElementById("textin-1").value;
    document.getElementById("textin-1").value = "";
    if (palabra.length > 0) {
      if (!existe_palabra(palabra.toLowerCase())) {
        palabras_instruidas.push(palabra.toLowerCase());
        meta_intru += 1;
      }

      if (document.getElementById("list-in-1_" + ensayo).textContent != "") {
        document.getElementById("list-in-1_" + ensayo).textContent =
          document.getElementById("list-in-1_" + ensayo).textContent +
          ", " +
          palabra.toLowerCase() +
          " (" +
          posicion +
          ")";
      } else {
        document.getElementById("list-in-1_" + ensayo).textContent =
          palabra.toLowerCase() + " (" + posicion + ")";
      }
      posicion++;
    } else {
      document.getElementById("text-modal-ord").textContent = "Campo vacío";
      document.getElementById("box-modal-ord").style.width = "20%";
      document.getElementById("modal-ord").style.display = "block";
    }
  }
}

// Procedimiento que anota la palabra seleccionada dentro de la página
function apuntarPalabra(fila) {
  click_metamemoria.play();
  if (
    document.getElementById("list-" + ensayo + "_ord-" + fila).textContent == ""
  ) {
    document.getElementById("list-" + ensayo + "_ord-" + fila).textContent =
      posicion;
    total_palabras += 1;
  } else {
    meta_persev += 1;
  }
  posicion++;
}

// Procedimiento que verifica si el ensayo es correcto
function verificarLista() {
  click_metamemoria.play();
  if (ensayo <= 5) {
    document.getElementById("text-modal-ord").textContent = "Siguiente ensayo";
    document.getElementById("box-modal-ord").style.width = "20%";
    document.getElementById("modal-ord").style.display = "block";
    document.getElementById("total_meta-" + ensayo).textContent =
      total_palabras;

    resultado =
      parseInt(
        document.getElementById("predictor_valor-" + ensayo).textContent
      ) - total_palabras;

    if (resultado > 0) {
      document.getElementById("error_meta-" + ensayo).textContent = resultado;
      // incrementa error positivo
      meta_errpos += resultado;
    } else {
      document.getElementById("error_meta-" + ensayo).textContent =
        resultado * -1;
      // incrementa error negativo
      meta_errneg += resultado * -1;
    }

    if (ensayo == 5) {
      iniciarPanel(true);
      document.getElementById("predictor").disabled = true;
      document.getElementById("reiniciar_metamemoria").disabled = true;

      document.getElementById("text-modal-ord").textContent = "Prueba finalizada";
      document.getElementById("box-modal-ord").style.width = "20%";
      document.getElementById("modal-ord").style.display = "block";
      window.completeMetamemory = true;
    } else {
      iniciarPanel(true);
    }
  }
  total_palabras = 0;
  ensayo++;
  posicion = 1;
  document.getElementById("btnModal-ord").onclick = function () {
    click_metamemoria.play();
    document.getElementById("modal-ord").style.display = "none";
  };
}

// Función que evalua si la palabra es una intrusión
function existe_palabra(palabra) {
  let seeker = false;

  for (x of palabras_instruidas) {
    if (x == palabra) {
      meta_persev += 1;
      seeker = true;
      break;
    }
  }
  return seeker;
}

// Procedimiento que habilita o deshabilita los elementos de la prueba
function iniciarPanel(estado) {
  document.getElementById("btn-1").disabled = estado;
  document.getElementById("btn-2").disabled = estado;
  document.getElementById("btn-3").disabled = estado;
  document.getElementById("btn-4").disabled = estado;
  document.getElementById("btn-5").disabled = estado;
  document.getElementById("btn-6").disabled = estado;
  document.getElementById("btn-7").disabled = estado;
  document.getElementById("btn-8").disabled = estado;
  document.getElementById("btn-9").disabled = estado;
  document.getElementById("textin-1").disabled = estado;
  document.getElementById("sigensayo-1").disabled = estado;
  document.getElementById("predictor").disabled = !estado;
}

// Procedimiento que muestra los datos en página
function mostrarMetamemoria() {
  document.getElementById("intrusion_metamemoria").textContent = meta_intru;
  document.getElementById("perseveracion_metamemoria").textContent =
    meta_persev;
  document.getElementById("err-positivo_metamemoria").textContent = meta_errpos;
  document.getElementById("err-negativo_metamemoria").textContent = meta_errneg;
  document.getElementById("err-total_metamemoria").textContent =
    meta_errpos + meta_errneg;
}

// Procedimiento que reinicia la prueba 
function limpiarMetamemoria() {
  location.reload();
  iniciarPanel(true);
  click_metamemoria.play();
  window.completeMetamemory = false;
}
