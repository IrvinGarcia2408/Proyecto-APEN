var click_fluidez = document.querySelector(".figure-sound");
var valores_fluidez = new Array(39);
var aciertos = 0;
var intrusiones = 0;
var perseveraciones = 0;

// Procedimiento que contabiliza el estado del verbo
function contarFluidez(tipo, posicion) {
  click_fluidez.play();
  if (document.getElementById("verbo_" + posicion).value != "") {
    buscarExistencias(posicion);

    if (tipo == "acierto") {
      aciertos++;
    } else if (tipo == "intrusion") {
      intrusiones++;
    } else if (tipo == "perseveracion") {
      perseveraciones++;
    }
    valores_fluidez[posicion - 1] = tipo;
  } else {
    document.getElementById("text-modal-fluidez").textContent =
      "Debes llenar el campo del verbo " + posicion;
    document.getElementById("box-modal-fluidez").style.width = "30%";
    document.getElementById("modal-fluidez").style.display = "block";

    document.getElementById("btnModal-fluidez").onclick = function () {
      click_fluidez.play();
      document.getElementById("modal-fluidez").style.display = "none";
    };
  }
}

// Procedimiento que busca si ya fue calificado antes el verbo
function buscarExistencias(posicion) {
  if (valores_fluidez[posicion - 1] == "acierto") {
    aciertos--;
  } else if (valores_fluidez[posicion - 1] == "intrusion") {
    intrusiones--;
  } else if (valores_fluidez[posicion - 1] == "perseveracion") {
    perseveraciones--;
  }
}

// Procedimiento que muestra los datos de BANFE actualizados
function mostrarFluidez() {
  document.getElementById("aciertos_fluidez").textContent = aciertos;
  document.getElementById("intrusiones_fluidez").textContent = intrusiones;
  document.getElementById("perseveraciones_fluidez").textContent = perseveraciones;
}

// Procedimiento que limpie lo campos al reiniciar la prueba
function cleanFluency(){
  const start = 1; // Número inicial
  const end = 40;  // Número final
  
  for (let i = start; i <= end; i++) {
      const textbox = document.getElementById(`verbo_${i}`);
      if (textbox) {
          textbox.value = "";
      }
  }

  valores_fluidez.length = 0;
  aciertos = 0;
  intrusiones = 0;
  perseveraciones = 0;
  mostrarFluidez();
}