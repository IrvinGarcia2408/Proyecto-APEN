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

/*    Memoria de trabajo visoespacial    */
var click_memoria = document.querySelector(".figure-sound");
var alarma_memoria = document.querySelector(".alarma_sound");
var turno = document.querySelector(".turno_sound");
var iniciar_memoria = false;
var iniciar_secuencia = false;
var deshabilitados = false;

var nivel = 1;
var ensayo = 1;
var cont_clicks = 0;

var terminado = false;

// Procedimiento que inicia la prueba del lado del sujeto
function iniciarMemoria() {
  if (!iniciar_memoria) {
    document.getElementById("text-modal-memoria").textContent = "Ahora, se van a señalar algunas figuras en un orden preciso. Cuando termine, usted deberá señalar las figuras en el mismo orden en que fueron señaladas; no debe hablar en ningún momento. ¿Listo? Comience.";
    document.getElementById("box-modal-memoria").style.width = "40%";
    document.getElementById("modal-memoria").style.display = "block";
    document.getElementById("btnModal-memoria").onclick = function() {
      click_senalamiento.play();
      document.getElementById("modal-memoria").style.display = "none";
      document.getElementById("boton").disabled = false;

      setTimeout(() => {
        inhabilitarFiguras();
        mostrarSecuencia();
        iniciar_secuencia = true;
      }, "1000");
    }
  } else {
    if (!iniciar_secuencia) {
      if (nivel <= 4) {
        setTimeout(() => {
          inhabilitarFiguras();
          mostrarSecuencia();
          iniciar_secuencia = true;
        }, "1000");
      } else {
        //Terminar prueba
        inhabilitarFiguras();
        document.getElementById("text-modal-memoria").textContent = "Prueba finalizada";
        document.getElementById("box-modal-memoria").style.width = "20%";
        document.getElementById("modal-memoria").style.display = "block";
      }
    }
  }
  iniciar_memoria = true;
}

// Procedimiento que procesa cuando eliges una figura
function chooseFigure(element) {
  if (iniciar_memoria && !deshabilitados) {
    click_memoria.play();
    element.style.border = "5px solid #d12";
    element.style.borderRadius = "20%";
    element.style.opacity = 1;
    setTimeout(() => {
      element.style.border = "none";
    }, 500);
    cont_clicks++;
    DjangoPOST("./" + element.getAttribute("id"), [element.getAttribute("id"),""+cont_clicks,""+nivel]);
  }
}

// Procedimiento que evalua si la secuencia del sujeto es correcta
async function terminarSecuencia() {
  click_memoria.play();
  flag = await DjangoGET("./error/" + 1);
  if (flag.error == 1) {
    nivel++;
    iniciar_secuencia = false;
    cont_clicks = 0;
    ensayo = 1;
    iniciarMemoria();
  } else if (ensayo == 1) {
    ensayo = 2;
    cont_clicks = 0;
    iniciar_secuencia = false;
    iniciarMemoria();
  } else {
    // terminar prueba
    iniciar_memoria = false;
    DjangoPOST("./finalizar/" + 1, 1);
    inhabilitarFiguras();
    alarma_memoria.play();
    document.getElementById("text-modal-memoria").textContent = "Prueba finalizada";
    document.getElementById("box-modal-memoria").style.width = "20%";
    document.getElementById("modal-memoria").style.display = "block";
  }
}

// Procedimiento que muestra la secuencia del nivel correspondiente
function mostrarSecuencia() {
  switch (nivel) {
    case 1:
      encenderFigura(document.getElementById("casa"));
      setTimeout(() => {
        document.getElementById("casa").style.border = "none";
        encenderFigura(document.getElementById("pantalon"));
      }, "1000");
      setTimeout(() => {
        document.getElementById("pantalon").style.border = "none";
        encenderFigura(document.getElementById("martillo"));
      }, "2000");
      setTimeout(() => {
        document.getElementById("martillo").style.border = "none";
        encenderFigura(document.getElementById("cinturon"));
      }, "3000");
      setTimeout(() => {
        document.getElementById("cinturon").style.border = "none";
      }, "4000");
      setTimeout(() => {
        turno.play();
        document.getElementById("text-modal-memoria").textContent = "Tu turno";
        document.getElementById("box-modal-memoria").style.width = "20%";
        document.getElementById("modal-memoria").style.display = "block";
        habilitarFiguras();
      }, "4500");
      break;
    case 2:
      encenderFigura(document.getElementById("mano"));
      setTimeout(() => {
        document.getElementById("mano").style.border = "none";
        encenderFigura(document.getElementById("avion"));
      }, "1000");
      setTimeout(() => {
        document.getElementById("avion").style.border = "none";
        encenderFigura(document.getElementById("mesa"));
      }, "2000");
      setTimeout(() => {
        document.getElementById("mesa").style.border = "none";
        encenderFigura(document.getElementById("calceta"));
      }, "3000");
      setTimeout(() => {
        document.getElementById("calceta").style.border = "none";
        encenderFigura(document.getElementById("manzana"));
      }, "4000");
      setTimeout(() => {
        document.getElementById("manzana").style.border = "none";
      }, "5000");
      setTimeout(() => {
        turno.play();
        document.getElementById("text-modal-memoria").textContent = "Tu turno";
        document.getElementById("box-modal-memoria").style.width = "20%";
        document.getElementById("modal-memoria").style.display = "block";
        habilitarFiguras();
      }, "5500");
      break;
    case 3:
      encenderFigura(document.getElementById("hormiga"));
      setTimeout(() => {
        document.getElementById("hormiga").style.border = "none";
        encenderFigura(document.getElementById("guitarra"));
      }, "1000");
      setTimeout(() => {
        document.getElementById("guitarra").style.border = "none";
        encenderFigura(document.getElementById("ardilla"));
      }, "2000");
      setTimeout(() => {
        document.getElementById("ardilla").style.border = "none";
        encenderFigura(document.getElementById("foco"));
      }, "3000");
      setTimeout(() => {
        document.getElementById("foco").style.border = "none";
        encenderFigura(document.getElementById("platano"));
      }, "4000");
      setTimeout(() => {
        document.getElementById("platano").style.border = "none";
        encenderFigura(document.getElementById("hacha"));
      }, "5000");
      setTimeout(() => {
        document.getElementById("hacha").style.border = "none";
      }, "6000");
      setTimeout(() => {
        turno.play();
        document.getElementById("text-modal-memoria").textContent = "Tu turno";
        document.getElementById("box-modal-memoria").style.width = "20%";
        document.getElementById("modal-memoria").style.display = "block";
        habilitarFiguras();
      }, "6500");
      break;
    case 4:
      encenderFigura(document.getElementById("foco"));
      setTimeout(() => {
        document.getElementById("foco").style.border = "none";
        encenderFigura(document.getElementById("pez"));
      }, "1000");
      setTimeout(() => {
        document.getElementById("pez").style.border = "none";
        encenderFigura(document.getElementById("pluma"));
      }, "2000");
      setTimeout(() => {
        document.getElementById("pluma").style.border = "none";
        encenderFigura(document.getElementById("casa"));
      }, "3000");
      setTimeout(() => {
        document.getElementById("casa").style.border = "none";
        encenderFigura(document.getElementById("bicicleta"));
      }, "4000");
      setTimeout(() => {
        document.getElementById("bicicleta").style.border = "none";
        encenderFigura(document.getElementById("cinturon"));
      }, "5000");
      setTimeout(() => {
        document.getElementById("cinturon").style.border = "none";
        encenderFigura(document.getElementById("calceta"));
      }, "6000");
      setTimeout(() => {
        document.getElementById("calceta").style.border = "none";
      }, "7000");
      setTimeout(() => {
        turno.play();
        document.getElementById("text-modal-memoria").textContent = "Tu turno";
        document.getElementById("box-modal-memoria").style.width = "20%";
        document.getElementById("modal-memoria").style.display = "block";
        habilitarFiguras();
      }, "7500");
      break;
  }

  document.getElementById("btnModal-memoria").onclick = function() {
    click_senalamiento.play();
    document.getElementById("modal-memoria").style.display = "none";
  }
}

// Procedimiento que pone el color en la figura y produce el click
function encenderFigura(element) {
  element.style.border = "5px solid #d12";
  element.style.borderRadius = "20%";
  click_memoria.play();
}

// Procedimiento que inhabilita las figuras
function inhabilitarFiguras() {
  deshabilitados = true;
  document.getElementById("ardilla").disabled = true;
  document.getElementById("avion").disabled = true;
  document.getElementById("bicicleta").disabled = true;
  document.getElementById("pluma").disabled = true;
  document.getElementById("caballo").disabled = true;
  document.getElementById("calceta").disabled = true;
  document.getElementById("casa").disabled = true;
  document.getElementById("cepillo").disabled = true;
  document.getElementById("cinturon").disabled = true;
  document.getElementById("foco").disabled = true;
  document.getElementById("guitarra").disabled = true;
  document.getElementById("hacha").disabled = true;
  document.getElementById("hormiga").disabled = true;
  document.getElementById("mano").disabled = true;
  document.getElementById("manzana").disabled = true;
  document.getElementById("martillo").disabled = true;
  document.getElementById("mesa").disabled = true;
  document.getElementById("pantalon").disabled = true;
  document.getElementById("pez").disabled = true;
  document.getElementById("platano").disabled = true;
  document.getElementById("saco").disabled = true;
  document.getElementById("gato").disabled = true;
  document.getElementById("jarra").disabled = true;
  document.getElementById("carro").disabled = true;
  document.getElementById("estufa").disabled = true;
  document.getElementById("boton").disabled = true;
}

// Procedimiento que habilita las figuras
function habilitarFiguras() {
  deshabilitados = false;
  document.getElementById("ardilla").disabled = false;
  document.getElementById("avion").disabled = false;
  document.getElementById("bicicleta").disabled = false;
  document.getElementById("pluma").disabled = false;
  document.getElementById("caballo").disabled = false;
  document.getElementById("calceta").disabled = false;
  document.getElementById("casa").disabled = false;
  document.getElementById("cepillo").disabled = false;
  document.getElementById("cinturon").disabled = false;
  document.getElementById("foco").disabled = false;
  document.getElementById("guitarra").disabled = false;
  document.getElementById("hacha").disabled = false;
  document.getElementById("hormiga").disabled = false;
  document.getElementById("mano").disabled = false;
  document.getElementById("manzana").disabled = false;
  document.getElementById("martillo").disabled = false;
  document.getElementById("mesa").disabled = false;
  document.getElementById("pantalon").disabled = false;
  document.getElementById("pez").disabled = false;
  document.getElementById("platano").disabled = false;
  document.getElementById("saco").disabled = false;
  document.getElementById("gato").disabled = false;
  document.getElementById("jarra").disabled = false;
  document.getElementById("carro").disabled = false;
  document.getElementById("estufa").disabled = false;
  document.getElementById("boton").disabled = false;
}

// Procedimiento que evalúa del lado del aplicador si la prueba ya termino
function apagarMemoria(){
  if(document.getElementById("memoria_fin").textContent == 1 && !terminado){
    document.getElementById("text-modal-memoria").textContent = "Prueba finalizada";
    document.getElementById("box-modal-memoria").style.width = "20%";
    document.getElementById("modal-memoria").style.display = "block";
    
    document.getElementById("btnModal-memoria").onclick = function() {
      click_senalamiento.play();
      document.getElementById("modal-memoria").style.display = "none";
    }
    terminado = true;
  }
} 