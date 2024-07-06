var alarma = document.querySelector(".alarma_sound"),
  click_laberinto = document.querySelector(".figure-sound"),
  iniciar_laberinto = !1,
  pausar_laberinto = !1,
  laberintos = 0,
  tiempo_inicio = 0;

// Función para iniciar cada uno de los laberintos
function iniciarLaberintos() {
  // Reproduce el sonido de clic
  click_laberinto.play(),

    // Verifica si la prueba ya ha sido iniciada
    iniciar_laberinto
      ? pausar_laberinto && (
        // Si se pausó la prueba, continúa el tiempo y habilita los laberintos siguientes
        (control = setInterval(cronometroLaberintos, 10)),
        (tiempo_inicio = segundos),
        (pausar_laberinto = !1),
        habilitarLaberintos(laberintos + 1))
      : (
        // Si es la primera vez que se inicia la prueba, configura el tiempo y habilita el primer laberinto
        (control = setInterval(cronometroLaberintos, 10)),
        (tiempo_inicio = segundos),
        (document.getElementById("reiniciar_laberintos").disabled = !1),
        (iniciar_laberinto = !0),
        habilitarLaberintos(1),
        (document.getElementById("final-1").disabled = !1));
}

// Procedimiento que detiene el tiempo de cada laberinto
function pararLaberintos() {
  click_laberinto.play();
  pausar_laberinto = true;
  clearInterval(control);
  laberintos += 1;
  
  // Calcula y actualiza el promedio del tiempo de los laberintos completados
  document.getElementById("promedio").textContent = Math.round(parseInt(document.getElementById("segundosP1").textContent) / laberintos);
  
  // Muestra el tiempo transcurrido en el laberinto actual
  document.getElementById("tiempo-" + laberintos).textContent = parseInt(document.getElementById("segundosP1").textContent) - tiempo_inicio;

  // Habilita los botones de inicio y finalización del próximo laberinto si quedan laberintos por completar
  if (laberintos < 5) {
    document.getElementById("inicio_" + (laberintos + 1)).disabled = false;
    document.getElementById("final-" + (laberintos + 1)).disabled = false;
  } else {
    // Deshabilita el botón de reinicio si ya se han completado los 5 laberintos
    document.getElementById("reiniciar_laberintos").disabled = true;
  }

  // Deshabilita los botones de control del laberinto actual
  inhabilitarLaberintos(laberintos);
}

// Procedimiento que reinicia la prueba completa
function reiniciarLaberintos() {
  // Reproduce el sonido de clic
  click_laberinto.play();
  
  // Detiene el cronómetro y reinicia las variables de tiempo
  clearInterval(control);
  centesimas = segundos = 0;
  
  // Restaura el estado inicial de la prueba y deshabilita los botones correspondientes
  iniciar_laberinto = false;
  inhabilitarLaberintos(laberintos);
  document.getElementById("segundosP1").innerHTML = "0";
  document.getElementById("promedio").innerHTML = "0";
  document.getElementById("reiniciar_laberintos").disabled = true;
  document.getElementById("final-1").disabled = true;
  
  // Reinicia el contador de laberintos completados
  laberintos = 0;
}


// Procedimiento que funciona como cronometro de la prueba
function cronometroLaberintos() {
  let ageTime = 0;

  if(parseInt(age) < 8){
    ageTime = 300;
  }else{
    ageTime = 240;
  }

  if (segundos === ageTime) {  // Comprueba si han pasado 300 segundos
    document.getElementById("reiniciar_laberintos").disabled = true;  // Deshabilita el botón de reinicio
    alarma.play();  // Reproduce la alarma
    pararLaberintos();  // Detiene el cronómetro
    document.getElementById("text-modal-laberintos").textContent = "Prueba finalizada";  // Muestra un mensaje
    document.getElementById("box-modal-laberintos").style.width = "20%";  // Ajusta el ancho del modal
    document.getElementById("modal-laberintos").style.display = "block";  // Muestra el modal
    document.getElementById("btnModal-laberintos").onclick = function () {  // Configura el evento de clic en el botón del modal
      click_laberinto.play();  // Reproduce un sonido
      document.getElementById("modal-laberintos").style.display = "none";  // Oculta el modal
    };
  }
  
  if (centesimas < 99) { centesimas++; }  // Incrementa las centésimas
  
  if (centesimas == 99) { centesimas = -1; }  // Restablece las centésimas
  
  if (centesimas == 0) {  // Si las centésimas llegan a cero
    segundos++;  // Incrementa los segundos
    document.getElementById("segundosP1").innerHTML = "" + segundos;  // Actualiza el elemento HTML con los segundos
    
    if (laberintos > 0) {  // Calcula y muestra el promedio si hay laberintos completados
      document.getElementById("promedio").textContent = Math.round(parseInt(document.getElementById("segundosP1").textContent) / laberintos);
    } else {
      document.getElementById("promedio").textContent = "0";
    }
  }
}

// Procedimiento que va incrementando los errores de cada laberinto
function sumar(laberinto, error) {
  click_laberinto.play();  // Reproduce un sonido
  // Incrementa el contador de errores del laberinto específico
  document.getElementById(error + "-" + laberinto).textContent =
    parseInt(document.getElementById(error + "-" + laberinto).textContent, 10) + 1;
  
  // Incrementa el contador total de errores según el tipo de error
  switch (error) {
    case "toca":
      document.getElementById("total-toca").textContent =
        parseInt(document.getElementById("total-toca").textContent, 10) + 1;
      break;
    case "atraviesa":
      document.getElementById("total-atraviesa").textContent =
        parseInt(document.getElementById("total-atraviesa").textContent, 10) +
        1;
      break;
    case "atrapado":
      document.getElementById("total-atrapado").textContent =
        parseInt(document.getElementById("total-atrapado").textContent, 10) + 1;
      break;
  }
}

// Procedimiento que va decrementando los errores de cada laberinto
function restar(laberinto, error) {
  click_laberinto.play();  // Reproduce un sonido
  // Verifica si el contador de errores del laberinto específico es mayor que cero antes de restarlo
  if (document.getElementById(error + "-" + laberinto).textContent != 0) {
    // Decrementa el contador de errores del laberinto específico
    document.getElementById(error + "-" + laberinto).textContent =
      parseInt(
        document.getElementById(error + "-" + laberinto).textContent,
        10
      ) - 1;
    
    // Decrementa el contador total de errores según el tipo de error
    switch (error) {
      case "toca":
        document.getElementById("total-toca").textContent =
          parseInt(document.getElementById("total-toca").textContent, 10) - 1;
        break;
      case "atraviesa":
        document.getElementById("total-atraviesa").textContent =
          parseInt(document.getElementById("total-atraviesa").textContent, 10) -
          1;
        break;
      case "atrapado":
        document.getElementById("total-atrapado").textContent =
          parseInt(document.getElementById("total-atrapado").textContent, 10) -
          1;
        break;
    }
  }
}


// Procedimiento que habilita los botones del laberinto correspondiente
function habilitarLaberintos(laberinto) {
  // Itera sobre cada laberinto y habilita los botones correspondientes
  for (let i = 1; i <= laberinto; i++) {
    document.getElementById("res-toc-" + i).disabled = false;  // Habilita el botón de restar para "toca"
    document.getElementById("sum-toc-" + i).disabled = false;  // Habilita el botón de sumar para "toca"
    document.getElementById("res-atr-" + i).disabled = false;  // Habilita el botón de restar para "atraviesa"
    document.getElementById("sum-atr-" + i).disabled = false;  // Habilita el botón de sumar para "atraviesa"
    document.getElementById("res-enc-" + i).disabled = false;  // Habilita el botón de restar para "atrapado"
    document.getElementById("sum-enc-" + i).disabled = false;  // Habilita el botón de sumar para "atrapado"
  }
}


// Procedimiento que inhabilita los botones del laberinto correspondiente
function inhabilitarLaberintos(laberinto) {
  // Inhabilita los botones para cada laberinto
  for (let i = 1; i <= 5; i++) {
    document.getElementById("res-toc-" + i).disabled = true;
    document.getElementById("sum-toc-" + i).disabled = true;
    document.getElementById("res-atr-" + i).disabled = true;
    document.getElementById("sum-atr-" + i).disabled = true;
    document.getElementById("res-enc-" + i).disabled = true;
    document.getElementById("sum-enc-" + i).disabled = true;
  }

  // Inhabilita botones de inicio y final según el laberinto
  if (laberinto >= 1) {
    if (laberinto > 1) {
      document.getElementById("inicio_" + laberinto).disabled = true;
      document.getElementById("final-" + laberinto).disabled = true;
    } else {
      document.getElementById("final-" + laberinto).disabled = true;
    }
  }

  // Limpia la tabla cuando es reiniciada
  if (!iniciar_laberinto) {
    for (let i = 1; i <= 5; i++) {
      document.getElementById("toca-" + i).innerHTML = "0";
      document.getElementById("atraviesa-" + i).innerHTML = "0";
      document.getElementById("atrapado-" + i).innerHTML = "0";
      document.getElementById("tiempo-" + i).innerHTML = "0";
    }
    document.getElementById("total-toca").innerHTML = "0";
    document.getElementById("total-atraviesa").innerHTML = "0";
    document.getElementById("total-atrapado").innerHTML = "0";
  }
}
