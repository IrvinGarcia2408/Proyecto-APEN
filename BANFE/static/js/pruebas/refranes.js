let click_refranes = document.querySelector(".figure-sound");

let init_refran = false;

// Procedimiento que habilita la opción elegida por el sujeto para el refran
function elegirRefran(a, b, c, refran) {
  if (
    document.getElementById(b).checked ||
    document.getElementById(c).checked
  ) {
    document.getElementById(b).checked = false;
    document.getElementById(c).checked = false;
  }

  DjangoPOST("./" + document.getElementById(a).value, [
    refran,
    document.getElementById(a).value,
  ]);
}

// Procedimiento que finaliza la prueba
function terminarRefranes() {
  if (validarRespuestas()) {
    DjangoPOST("./terminar/" + 1, 1);
    document.getElementById("btn-terminar_refranes").disabled = true;
    for (let i = 1; i < 6; i++) {
      document.getElementById("a_" + i).disabled = true;
      document.getElementById("b_" + i).disabled = true;
      document.getElementById("c_" + i).disabled = true;
    }
    document.getElementById("text-modal-refranes").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-refranes").style.width = "20%";
    document.getElementById("modal-refranes").style.display = "block";
    document.getElementById("btn-terminar_refranes").disabled = true;
  } else {
    document.getElementById("text-modal-refranes").textContent =
      "Debes responder todos los refranes";
    document.getElementById("box-modal-refranes").style.width = "25%";
    document.getElementById("modal-refranes").style.display = "block";
  }
}

// Función que valida que todos los refranes hayan sido respondidos
function validarRespuestas() {
  if (
    document.getElementById("a_1").checked ||
    document.getElementById("b_1").checked ||
    document.getElementById("c_1").checked
  ) {
    if (
      document.getElementById("a_2").checked ||
      document.getElementById("b_2").checked ||
      document.getElementById("c_2").checked
    ) {
      if (
        document.getElementById("a_3").checked ||
        document.getElementById("b_3").checked ||
        document.getElementById("c_3").checked
      ) {
        if (
          document.getElementById("a_4").checked ||
          document.getElementById("b_4").checked ||
          document.getElementById("c_4").checked
        ) {
          if (
            document.getElementById("a_5").checked ||
            document.getElementById("b_5").checked ||
            document.getElementById("c_5").checked
          ) {
            return true;
          }
        }
      }
    }
  } else {
    return false;
  }
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
    body: JSON.stringify({ data: datos }),
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

// Procedimiento que inicia el cronometro del lado del aplicador
function inicioCronoRef() {
  click_refranes.play();
  control = setInterval(cronometroRefranes, 10);
  document.getElementById("inicio_refranes").disabled = true;
  document.getElementById("reiniciar_refranes").disabled = false;
}

// Procedimiento que reinicia el cronometro del lado del aplicador
function reinicioCronoRef() {
  click_refranes.play();
  clearInterval(control);
  centesimas = segundos = 0;
  document.getElementById("segundos_refranes").innerHTML = "0";
  document.getElementById("inicio_refranes").disabled = false;
  document.getElementById("reiniciar_refranes").disabled = true;
}

// Procedimiento que funciona como cronometro para el aplicador
function cronometroRefranes() {
  if (
    segundos == 300 ||
    document.getElementById("fin_refranes").textContent == 1
  ) {
    alarma.play();
    document.getElementById("reiniciar_refranes").disabled = true;
    clearInterval(control);
    document.getElementById("text-modal-refranes").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-refranes").style.width = "20%";
    document.getElementById("modal-refranes").style.display = "block";

    document.getElementById("btnModal-refranes").onclick = function () {
      click_refranes.play();
      document.getElementById("modal-refranes").style.display = "none";
    };
  }
  console.log("Segundos: " + segundos + " | Centesimas: " + centesimas);
  if (centesimas < 99) {
    centesimas++;
  }

  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
    document.getElementById("segundos_refranes").innerHTML = "" + segundos;
  }
}

// Procedimiento que funciona como cronometro para el sujeto
function reloj_refranes() {
  if (segundos == 300) {
    clearInterval(temporizador);

    for (let i = 1; i < 6; i++) {
      document.getElementById("a_" + i).disabled = true;
      document.getElementById("b_" + i).disabled = true;
      document.getElementById("c_" + i).disabled = true;
    }
    document.getElementById("text-modal-refranes").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-refranes").style.width = "20%";
    document.getElementById("modal-refranes").style.display = "block";
    document.getElementById("btn-terminar_refranes").disabled = true;
  }
  console.log("Segundos: " + segundos + " | Centesimas: " + centesimas);
  if (centesimas < 99) {
    centesimas++;
  }

  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
  }
}

function iniciaRefranes() {
  document.getElementById("text-modal-refranes").textContent =
    "Ahora, lo que tiene que hacer es leer cada uno de los refranes en voz alta y seleccionar cuál de las tres opciones de respuesta es la que mejor describe el significado de cada refrán. Comience.";
  document.getElementById("box-modal-refranes").style.width = "40%";
  document.getElementById("modal-refranes").style.display = "block";

  document.getElementById("btnModal-refranes").onclick = function () {
    click_refranes.play();
    document.getElementById("modal-refranes").style.display = "none";
    if (!init_refran) {
      temporizador = setInterval(reloj_refranes, 10);
      document.getElementById("btn-terminar_refranes").disabled = false;
      init_refran = true;
    }
  };

  for (let i = 1; i < 6; i++) {
    document.getElementById("a_" + i).disabled = false;
    document.getElementById("b_" + i).disabled = false;
    document.getElementById("c_" + i).disabled = false;
  }
}
