const alarmSignaling = document.querySelector(".alarmSignaling");

window.completeSignaling = false;

// Procedimiento que inicia el cronometro del lado del aplicador
function inicioCronoSen() {
  click_senalamiento.play();
  control = setInterval(cronometroSenalamiento, 10);
  document.getElementById("inicio").disabled = true;
  document.getElementById("reinicio").disabled = false;
}
// Procedimiento que reinicia el cronometro del lado del aplicador
function reinicioCronoSen() {
  click_senalamiento.play();
  clearInterval(control);
  centesimas = segundos = 0;
  document.getElementById("secondSignaling").innerHTML = "0";
  document.getElementById("inicio").disabled = false;
  document.getElementById("reinicio").disabled = true;
  window.completeSignaling = false;
}

// Procedimiento que funciona como cronometro para el aplicador
function cronometroSenalamiento() {
  if (segundos == 300 || document.getElementById("fin").textContent == 1) {
    alarmSignaling.play();
    clearInterval(control);
    document.getElementById("text-modal-sen").textContent = "Prueba finalizada";
    document.getElementById("box-modal-sen").style.width = "20%";
    document.getElementById("modal-sen").style.display = "block";
    document.getElementById("reinicio").disabled = true;
    
    document.getElementById("btnModal-sen").onclick = function() {
      click_senalamiento.play();
      document.getElementById("modal-sen").style.display = "none";
    }
    window.completeSignaling = true;
  }
  if (centesimas < 99) {
    centesimas++;
  }

  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
    document.getElementById("secondSignaling").innerHTML = "" + segundos;
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

/*    Señalamiento autodirigido    */
let click_senalamiento = document.querySelector(".figure-sound");
let iniciar_senalamiento = false;

let secondsSignaling = 0;
let hundrethsSignaling = 0;


// Procedimiento que inicia la prueba del lado del sujeto
function iniciarSenalamiento(){
  if(!iniciar_senalamiento){
    document.getElementById("text-modal-sen").textContent = "Ahora, en esta lámina haga click en una figura distinta cada vez. Las figuras que seleccione no deben estar juntas, debe señalarlas de forma salteada; por ejemplo, si señala la ardilla, no puede señalar la que está a su derecha (avión), ni la que está abajo (calcetín) o la que está en diagonal (casa). Debe señalar todas las figuras, pero trate de no repetir ninguna. Avíseme cuando haya terminado.";
    document.getElementById("box-modal-sen").style.width = "40%";
    document.getElementById("modal-sen").style.display = "block";
    
    document.getElementById("btnModal-sen").onclick = function() {
      click_senalamiento.play();
      iniciar_senalamiento = true;
      document.getElementById("modal-sen").style.display = "none";
      if(document.getElementById("text-modal-sen").textContent != "Prueba finalizada"){
        temporizador = setInterval(reloj_senalamiento, 10);
        
        
        document.getElementById("btn-terminar_senalamiento").disabled = false;
      }
    }
    
  }
}

// Procedimiento que procesa la figura dada y muestra la selección de la misma
function selectFigure(element) {
  if (iniciar_senalamiento) {
    click_senalamiento.play();
    element.style.border = "5px solid #d12";
    element.style.borderRadius = "20%";
    element.style.opacity = 1;
    setTimeout(() => {
      element.style.border = "none";
    }, 500);
    DjangoPOST("./" + element.getAttribute("id"), element.getAttribute("id"));
  }
}

// Procedimiento que termina la prueba
function terminarSenalamiento() {
  if (iniciar_senalamiento) {
    DjangoPOST("./" + 1, 1);
    clearInterval(temporizador);
    document.getElementById("text-modal-sen").textContent = "Prueba finalizada"
    document.getElementById("box-modal-sen").style.width = "20%";
    document.getElementById("modal-sen").style.display = "block";
    document.getElementById("btn-terminar_senalamiento").disabled = true;

    // Cargar resultados a BD, porque despues se borran
  }
}

// Procedimiento que funciona como cronometro para el sujeto
function reloj_senalamiento() {
  if (secondsSignaling == 300) {
    clearInterval(temporizador);
    document.getElementById("text-modal-sen").textContent = "Prueba finalizada"
    document.getElementById("box-modal-sen").style.width = "20%";
    document.getElementById("modal-sen").style.display = "block";
    document.getElementById("btn-terminar_senalamiento").disabled = true;
  }
  if (hundrethsSignaling < 99) {
    hundrethsSignaling++;
  }

  if (hundrethsSignaling == 99) {
    hundrethsSignaling = -1;
  }
  if (hundrethsSignaling == 0) {
    secondsSignaling++;
  }
}
