
let click_clcartas = document.querySelector(".figure-sound");
let segundos_clasif = 0;
let centesimas_clasif = 0;

// Procedimiento que inicia el reloj para el aplicador
function inicio() {  
  click_clcartas.play();
  control = setInterval(cronometro, 10);
  document.getElementById("inicio").disabled = true;
  document.getElementById("reinicio").disabled = false;
}

// Procedimiento que detiene el reloj del lado del aplicador
function parar() {
  clearInterval(control);
  document.getElementById("reinicio").disabled = true;
}

// Procedimiento que reinicia el reloj del lado del aplicador
function reinicio() {
  click_clcartas.play();
  clearInterval(control);
  centesimas_clasif = segundos_clasif = 0;
  document.getElementById("segundos").innerHTML = "0";
  document.getElementById("inicio").disabled = false;
  document.getElementById("reinicio").disabled = true;
}

// Procedimiento que funciona como cronometro del lado del aplicador
function cronometro() {
  let cartas =
    parseInt(document.getElementById("aciertos_cards_sorting").textContent, 10) +
    parseInt(document.getElementById("errores_cards_sorting").textContent, 10) +
    parseInt(document.getElementById("perseveraciones_cards_sorting").textContent, 10) +
    parseInt(document.getElementById("err-mto_cards_sorting").textContent, 10) +
    parseInt(document.getElementById("pers-dif_cards_sorting").textContent, 10);
  if (cartas == 64 || segundos_clasif == 600) {
    alarma.play();
    parar();
    document.getElementById("text-modal-clas").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-clas").style.width = "20%";
    document.getElementById("modal-clas").style.display = "block";

    document.getElementById("btnModal-clas").onclick = function () {
      click_clcartas.play();
      document.getElementById("modal-clas").style.display = "none";
    };
  }
  console.log("Segundos: " + segundos_clasif + " | Centesimas: " + centesimas_clasif);
  if (centesimas_clasif < 99) {
    centesimas_clasif++;
  }

  if (centesimas_clasif == 99) {
    centesimas_clasif = -1;
  }
  if (centesimas_clasif == 0) {
    segundos_clasif++;
    document.getElementById("segundos").innerHTML = "" + segundos_clasif;
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

/*    Clasificacion de cartas     */
let carta = 1;
let mano = false;
let activo = false;
let audio = document.querySelector(".carta_sound");
let incorrecto = document.querySelector(".incorrecto_sound");
let second_cards = 0;
let hundredths_cards = 0;


window.onload = function() {
  // Selecciona todas las imágenes dentro de los elementos <div> con la clase 'panel-cartas__vacio'
  var images = document.querySelectorAll('.panel-cartas__vacio div img');
  
  // Itera sobre todas las imágenes seleccionadas
  images.forEach(function(image) {
      // Verifica si la imagen no tiene una URL de origen (src)
      if (!image.src || image.src.includes('0.jpeg')) {
          // Oculta la imagen si la URL de la imagen es igual a la URL de la imagen de relleno
          image.style.display = 'none';
      }
  });
};


// Procedimiento que inicia la prueba para el sujeto
function iniciarClasificacion() {
  if (carta == 1 && !activo) {
    document.getElementById("text-modal-clas").textContent =
      "En esta tarea lo que tiene que hacer es tomar cada una de las cartas que se encuentran al lado izquierdo de la pantalla y debe colocarlas en los espacios vacíos, según como crea que se relacionan o deban clasificarse con respecto a la carta que está al frente del espacio. Los criterios de clasificación irán cambiando conforme avance la prueba. Si la carta que colocó es correcta, no escuchará nada, pero si es incorrecta, escuchará 'incorrecto', entonces tomará la siguiente carta y trate de colocarla en el lugar adecuado. ¿Listo?";
    document.getElementById("box-modal-clas").style.width = "40%";
    document.getElementById("modal-clas").style.display = "block";
    document.getElementById("btnModal-clas").onclick = function () {
      click_clcartas.play();
      document.getElementById("modal-clas").style.display = "none";
      if (activo) {
        temporizador = setInterval(reloj, 10);
      }
    };
  }
  activo = true;
}

//  Prodemiento para tomar una carta
function takeCard() {
  if (carta <= 64 && activo) {
    if (!mano) {
      audio.play();
      document.getElementById("espacio1").style.cssText =
        "border: 6px solid rgb(255,255,100);";
      document.getElementById("espacio2").style.cssText =
        "border: 6px solid rgb(255,255,100);";
      document.getElementById("espacio3").style.cssText =
        "border: 6px solid rgb(255,255,100);";
      document.getElementById("espacio4").style.cssText =
        "border: 6px solid rgb(255,255,100);";
      mano = true;
      // Peticiones a Views.py
      DjangoPOST("./" + carta, carta);
    }
  }
}

//  Procedimiento para colocar la carta en uno de los espacios
async function putCard(opcion) {
  if (mano & activo) {
    document.getElementById("espacio1").style.cssText =
      "border: #333 solid 3px;";
    document.getElementById("espacio2").style.cssText =
      "border: #333 solid 3px;";
    document.getElementById("espacio3").style.cssText =
      "border: #333 solid 3px;";
    document.getElementById("espacio4").style.cssText =
      "border: #333 solid 3px;";
    document.getElementById("torre").src =
      "/static/imagenes/clasif-cartas/" + (carta += 1) + ".jpeg";     
    switch (opcion) {
      case "A":
        document.getElementById("espacioA").src =
          "/static/imagenes/clasif-cartas/" + (carta - 1) + ".jpeg";
        document.getElementById("espacioA").style.display = 'block';          
        DjangoPOST("./A", "A");
        setTimeout(() => {
          sonarError();
        }, 350);
        break;
      case "B":
        document.getElementById("espacioB").src =
          "/static/imagenes/clasif-cartas/" + (carta - 1) + ".jpeg";
        document.getElementById("espacioB").style.display = 'block';           
        DjangoPOST("./B", "B");
        setTimeout(() => {
          sonarError();
        }, 350);
        break;
      case "C":
        document.getElementById("espacioC").src =
          "/static/imagenes/clasif-cartas/" + (carta - 1) + ".jpeg";
        document.getElementById("espacioC").style.display = 'block';           
        DjangoPOST("./C", "C");
        setTimeout(() => {
          sonarError();
        }, 350);
        break;
      case "D":
        document.getElementById("espacioD").src =
          "/static/imagenes/clasif-cartas/" + (carta - 1) + ".jpeg";
        document.getElementById("espacioD").style.display = 'block';          
        DjangoPOST("./D", "D");
        setTimeout(() => {
          sonarError();
        }, 350);
        break;
      default:
        document.getElementById("text-modal-clas").textContent =
          "Movimiento no válido";
        document.getElementById("box-modal-clas").style.width = "20%";
        document.getElementById("modal-clas").style.display = "block";
        document.getElementById("btnModal-clas").onclick = function () {
          click_clcartas.play();
          document.getElementById("modal-clas").style.display = "none";
        };
        break;
    }
    mano = false;
    audio.play();
  }
}

// Procedimiento que reproduce el sonido de error
async function sonarError() {
  sonido = await DjangoGET("./todas/" + 1);
  if (sonido.error == 1) {
    incorrecto.play();
  }
}

// Procedimiento que funciona como cronometro para el sujeto
function reloj() {
  if (carta > 64 || second_cards == 600) {
    document.getElementById("torre").src =
      "/static/imagenes/clasif-cartas/" + (carta += 1) + ".jpeg";
    document.getElementById("torre").style.display = 'none';        
    
    clearInterval(temporizador);
    activo = false;
    document.getElementById("text-modal-clas").textContent =
      "Prueba finalizada";
    document.getElementById("box-modal-clas").style.width = "20%";
    document.getElementById("modal-clas").style.display = "block";
    document.getElementById("torre").disabled = true;

    document.getElementById("btnModal-clas").onclick = function () {
      click_clcartas.play();
      document.getElementById("modal-clas").style.display = "none";
    };
  }
  console.log("Segundos: " + second_cards + " | Centesimas: " + hundredths_cards);
  if (hundredths_cards < 99) {
    hundredths_cards++;
  }

  if (hundredths_cards == 99) {
    hundredths_cards = -1;
  }
  if (hundredths_cards == 0) {
    second_cards++;
  }
}
