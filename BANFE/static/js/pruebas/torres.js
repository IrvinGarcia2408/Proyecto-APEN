// Variables
let click_torres = document.querySelector(".figure-sound"),
    segundos_2 = 0,
    centesimas_2 = 0,
    torres_flag = 1,
    mov = 0,
    err_1 = 0,
    err_2 = 0;

// Procedimiento para iniciar las torres
function iniciarTorres() {
  // Reproducir sonido de click
  click_torres.play();
  // Iniciar cronómetro de la primera o segunda torre según la bandera
  control = setInterval(torres_flag == 1 ? cronometroTorres_1 : cronometroTorres_2, 10);
  activarContadores(torres_flag);

  // Deshabilitar botones al iniciar la prueba
  document.querySelectorAll("#inicio_torre, #parar_torre, #reiniciar_torre").forEach(btn => btn.disabled = true);
  document.getElementById("parar_torre").disabled = false;
  document.getElementById("reiniciar_torre").disabled = false;
  if(torres_flag === 1){
    if (parseInt(age) < 10) {
      document.getElementById("progreso-torres").textContent ="1 / 1";
      document.getElementById("siguiente_torre").disabled = true;
    }else{
      document.getElementById("progreso-torres").textContent ="1 / 2";
    }
  }
}

// Procedimiento para mostrar un modal con un mensaje y ejecutar una función al cerrarlo
function mostrarModal(mensaje, callback) {
  document.getElementById("text-modal-chron").textContent = mensaje;
  document.getElementById("box-modal-chron").style.width = "20%";
  document.getElementById("modal-chron").style.display = "block";
  document.getElementById("btnModal-chron").onclick = function() {
    click_torres.play();
    document.getElementById("modal-chron").style.display = "none";
    if (callback) callback();
  };
}

// Procedimiento que detiene la torre correspondiente
function pararTorres() {
  // Reproducir sonido de click
  click_torres.play();

  if (torres_flag == 1) {
    // Deshabilitar botones y avanzar a la siguiente torre
    document.getElementById("inicio_torre").disabled = true;
    document.getElementById("parar_torre").disabled = true;
    document.getElementById("siguiente_torre").disabled = false;
    document.getElementById("reiniciar_torre").disabled = true;
    if (parseInt(age) < 10) {
      document.getElementById("siguiente_torre").disabled = true;
    }
    torres_flag = 2;
  } else if (torres_flag == 2) {
    // Deshabilitar botones y mostrar modal de prueba finalizada
    document.getElementById("inicio_torre").disabled = true;
    document.getElementById("parar_torre").disabled = true;
    document.getElementById("reiniciar_torre").disabled = true;
    torres_flag = 0;
    mostrarModal("Prueba finalizada");
  }

  // Configurar evento de clic en el botón del modal
  document.getElementById("btnModal-chron").onclick = function() {
    click_torres.play();
    document.getElementById("modal-chron").style.display = "none";
  }

  // Detener el cronómetro
  clearInterval(control);
}

// Procedimiento que avanza a la siguiente torre
function siguienteTorre() {
  // Verificar edad para avanzar a la siguiente torre
  if(parseInt(age) >= 10){
    click_torres.play();
    // Mostrar elementos de la siguiente torre y reiniciar contadores
    document.getElementById("progreso-torres").textContent ="2 / 2";
    document.getElementById("reloj-torre-1").className = "apagado";
    document.getElementById("control-torre-1").className = "apagado";
    document.getElementById("resultados-torre-1").className = "apagado";
    document.getElementById("reloj-torre-2").classList.remove("apagado");
    document.getElementById("control-torre-2").classList.remove("apagado");
    document.getElementById("resultados-torre-2").classList.remove("apagado");
    document.getElementById("inicio_torre").disabled = false;
    mov = err_1 = err_2 = 0;
  }
  // Deshabilitar botón de siguiente torre
  document.getElementById("siguiente_torre").disabled = true;
}


// Procedimiento para reiniciar cada torre
function reiniciarTorres() {
  // Reproducir sonido de click
  click_torres.play();
  // Detener el cronómetro
  clearInterval(control);
  
  // Reiniciar variables y limpiar torres correspondientes
  if (torres_flag == 1) {
    centesimas = segundos = 0;
    limpiarTorres(torres_flag);
    document.getElementById("segundos_torres-1").innerHTML = "0";
  } else {
    centesimas_2 = segundos_2 = 0;
    limpiarTorres(torres_flag);
    document.getElementById("segundos_torres-2").innerHTML = "0";
  }
  
  // Habilitar botones adecuados al reiniciar
  document.getElementById("inicio_torre").disabled = false;
  document.getElementById("parar_torre").disabled = true;
  document.getElementById("siguiente_torre").disabled = true;
  document.getElementById("reiniciar_torre").disabled = true;
}

// Inicializar variable para controlar el tiempo de la prueba de la torre A
let ageTime = 0;

// Procedimiento que funciona como cronómetro de la torre A
function cronometroTorres_1() {
  // Establecer el tiempo máximo de la prueba según la edad del sujeto
  if (parseInt(age) < 8) {
    ageTime = 300;
  } else {
    ageTime = 240;
  }

  // Comprobar si se alcanzó el tiempo máximo de la prueba
  if (segundos === ageTime) {
    // Reproducir alarma y detener la prueba
    alarma.play();
    torres_flag = 0;
    pararTorres();
    // Mostrar mensaje de finalización de la prueba en un modal
    mostrarModal("Prueba finalizada")
  }

  // Actualizar centésimas de segundo
  if (centesimas < 99) {
    centesimas++;
  }
  if (centesimas == 99) {
    centesimas = -1;
  }

  // Actualizar segundos y mostrarlos en el elemento HTML
  if (centesimas == 0) {
    segundos++;
    document.getElementById("segundos_torres-1").innerHTML = "" + segundos;
  }
}

// Procedimiento que funciona como cronómetro de la torre B
function cronometroTorres_2() {
  // Comprobar si se alcanzó el tiempo máximo de la prueba
  if (segundos_2 == ageTime - segundos) {
    // Reproducir alarma y detener la prueba
    alarma.play();
    pararTorres();
    torres_flag = 0;
    // Mostrar mensaje de finalización de la prueba en un modal
    mostrarModal("Prueba finalizada")
  }

  // Actualizar centésimas de segundo
  if (centesimas_2 < 99) {
    centesimas_2++;
  }
  if (centesimas_2 == 99) {
    centesimas_2 = -1;
  }

  // Actualizar segundos y mostrarlos en el elemento HTML
  if (centesimas_2 == 0) {
    segundos_2++;
    document.getElementById("segundos_torres-2").innerHTML = "" + segundos_2;
  }
}


// Procedimiento que limpia la torre correspondiente
function limpiarTorres(torre) {
  // Reinicia todas las variables relacionadas con la torre
  mov = err_1 = err_2 = 0;
  
  // Selecciona los elementos HTML correspondientes y los reinicia
  const movElement = document.getElementById(`mov-torre-${torre}`);
  const err1Element = document.getElementById(`err_1-${torre}`);
  const err2Element = document.getElementById(`err_2-${torre}`);
  const totalErrElement = document.getElementById(`err_total-${torre}`);
  
  movElement.textContent = 0;
  err1Element.textContent = 0;
  err2Element.textContent = 0;
  totalErrElement.textContent = 0;
  
  // Deshabilita los botones de contadores
  document.getElementById(`ac_res-torre-${torre}`).disabled = true;
  document.getElementById(`ac_sum-torre-${torre}`).disabled = true;
  document.getElementById(`err_1_res-torre-${torre}`).disabled = true;
  document.getElementById(`err_1_sum-torre-${torre}`).disabled = true;
  document.getElementById(`err_2_res-torre-${torre}`).disabled = true;
  document.getElementById(`err_2_sum-torre-${torre}`).disabled = true;
}

// Procedimiento que incrementa o decrementa cada variable BANFE involucrada
function anotarTorre(resta, tipo) {
  // Reproduce el sonido del contador
  click_torres.play();
  
  // Incrementa o decrementa la variable correspondiente según el tipo
  if (tipo == "movimiento") {
    if ((mov != 0 && resta == -1) || resta == 1) {
      mov += resta;
    }
  } else if (tipo == "error_1") {
    if ((err_1 != 0 && resta == -1) || resta == 1) {
      err_1 += resta;
    }
  } else if (tipo == "error_2") {
    if ((err_2 != 0 && resta == -1) || resta == 1) {
      err_2 += resta;
    }
  }

  // Actualiza los elementos HTML con los nuevos valores
  if(torres_flag != 0){
    document.getElementById(`mov-torre-${torres_flag}`).textContent = mov;
    document.getElementById(`err_1-${torres_flag}`).textContent = err_1;
    document.getElementById(`err_2-${torres_flag}`).textContent = err_2;
    document.getElementById(`err_total-${torres_flag}`).textContent = err_1 + err_2;
  }
}

// Procedimiento que muestra los datos de BANFE actualizados
function mostrarTorres() {
  // Selecciona los elementos HTML correspondientes y los actualiza según la torre actual
  if(torres_flag != 0){
    const movElement = document.getElementById(`mov-torre-${torres_flag}`);
    const err1Element = document.getElementById(`err_1-${torres_flag}`);
    const err2Element = document.getElementById(`err_2-${torres_flag}`);
    const totalErrElement = document.getElementById(`err_total-${torres_flag}`);  
  
    movElement.textContent = mov;
    err1Element.textContent = err_1;
    err2Element.textContent = err_2;
    totalErrElement.textContent = err_1 + err_2;
  }
}

// Procedimiento que habilita los botones contadores
function activarContadores(nivel) {
  // Habilita los botones de contador correspondientes a la torre
  document.getElementById(`ac_res-torre-${nivel}`).disabled = false;
  document.getElementById(`ac_sum-torre-${nivel}`).disabled = false;
  document.getElementById(`err_1_res-torre-${nivel}`).disabled = false;
  document.getElementById(`err_1_sum-torre-${nivel}`).disabled = false;
  document.getElementById(`err_2_res-torre-${nivel}`).disabled = false;
  document.getElementById(`err_2_sum-torre-${nivel}`).disabled = false;
}

