
var suma = 1;
var result_ant = "ninguno";
var aciertos = 0;
var errores = 0;
var pausado = false;
var num_ant = 1;

var resta= [40,100];
var ac_resta = [0,0];
var err_resta = [0,0];
var res_flag = 1;
var x = 0;

var click_resum = document.querySelector(".figure-sound");

// Procedimiento que inicia la suma
function iniciarSuma() {
  click_resum.play();
  apagarSuma(false);
  document.getElementById("sum-6").focus();
  control = setInterval(cronometroSuma, 10);
  document.getElementById("inicio_suma").disabled = true;
  document.getElementById("reiniciar_suma").disabled = false;
}

// Procedimiento que detiene la suma
function pararSuma() {
  clearInterval(control);
  document.getElementById("reiniciar_suma").disabled = true;
  apagarSuma(true);
}

// Procedimiento que reinicia la suma
function reiniciarSuma() {
  click_resum.play();
  clearInterval(control);
  centesimas = segundos = 0;
  document.getElementById("segundos_suma").innerHTML = "0";
  document.getElementById("inicio_suma").disabled = false;
  document.getElementById("reiniciar_suma").disabled = true;
  limpiarSuma();
  apagarSuma(true);
}

// Procedimiento que funciona como cronometro de la prueba
function cronometroSuma() {
  if (segundos == 300) {
    alarma.play();
    pararSuma();
    document.getElementById("text-modal-sum").textContent = "Prueba finalizada"
    document.getElementById("box-modal-sum").style.width = "20%";
    document.getElementById("modal-sum").style.display = "block";
    document.getElementById("btnModal-sum").onclick = function() {
      click_resum.play();
      document.getElementById("modal-sum").style.display = "none";
    }
  }
  if (centesimas < 99) {
    centesimas++;
  }

  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
    document.getElementById("segundos_suma").innerHTML = "" + segundos;
  }
}

// Procedimiento que toma el valor dado en cada campo de texto
function presionarTecla(checkbox,textbox,text_sig){
    text = document.getElementById(textbox).value;
    valor = document.getElementById(textbox).placeholder;

    if (event.key == "Enter"){
        if(document.getElementById(checkbox).checked){
          if(text==null){
            suma -= num_ant;
          }else{
            suma -= num_ant;
          }
          if(result_ant == "acierto"){
            aciertos -= 1;
          }else if(result_ant == "error"){
            errores -= 1;
          }
        }else{
          document.getElementById(checkbox).checked = true;
        }

        if(text_sig != null){
          document.getElementById(text_sig).focus();
        }

        validarSuma(text,valor);
    }
}

// Procedimiento que valida que el valor recibido sea correcto
function validarSuma(text,valor){
    if (text.length == 0) {
        if(parseInt(valor,10) == (suma+5)){
            result_ant = "acierto";
            aciertos += 1;
            suma += 5;
            num_ant = 5;
        }else{
            result_ant = "error";
            errores += 1;
            num_ant = parseInt(valor,10) - suma;
            suma = parseInt(valor,10);
        }
       
    }else{
        if(parseInt(text,10) == (suma+5)){
            result_ant = "acierto";
            aciertos += 1;
            suma += 5;
            num_ant = 5;
        }else{
            result_ant = "error";
            errores += 1;
            num_ant = parseInt(text,10) - suma;
            suma = parseInt(text,10);
        }
    }
    document.getElementById("aciertos-suma").innerHTML = aciertos;
    document.getElementById("errores-suma").innerHTML = errores;

    if((aciertos + errores) == 20){
      pararSuma();
    }
}

// Procedimiento que inhabilita los campos de la prueba 
function apagarSuma(valor){
  document.getElementById("check-sum-6").disabled = valor;
  document.getElementById("sum-6").disabled = valor;
  document.getElementById("check-sum-11").disabled = valor;
  document.getElementById("sum-11").disabled = valor;
  document.getElementById("check-sum-16").disabled = valor;
  document.getElementById("sum-16").disabled = valor;
  document.getElementById("check-sum-21").disabled = valor;
  document.getElementById("sum-21").disabled = valor;
  document.getElementById("check-sum-26").disabled = valor;
  document.getElementById("sum-26").disabled = valor;
  document.getElementById("check-sum-31").disabled = valor;
  document.getElementById("sum-31").disabled = valor;
  document.getElementById("check-sum-36").disabled = valor;
  document.getElementById("sum-36").disabled = valor;
  document.getElementById("check-sum-41").disabled = valor;
  document.getElementById("sum-41").disabled = valor;
  document.getElementById("check-sum-46").disabled = valor;
  document.getElementById("sum-46").disabled = valor;
  document.getElementById("check-sum-51").disabled = valor;
  document.getElementById("sum-51").disabled = valor;
  document.getElementById("check-sum-56").disabled = valor;
  document.getElementById("sum-56").disabled = valor;
  document.getElementById("check-sum-61").disabled = valor;
  document.getElementById("sum-61").disabled = valor;
  document.getElementById("check-sum-66").disabled = valor;
  document.getElementById("sum-66").disabled = valor;
  document.getElementById("check-sum-71").disabled = valor;
  document.getElementById("sum-71").disabled = valor;
  document.getElementById("check-sum-76").disabled = valor;
  document.getElementById("sum-76").disabled = valor;
  document.getElementById("check-sum-81").disabled = valor;
  document.getElementById("sum-81").disabled = valor;
  document.getElementById("check-sum-86").disabled = valor;
  document.getElementById("sum-86").disabled = valor;
  document.getElementById("check-sum-91").disabled = valor;
  document.getElementById("sum-91").disabled = valor;
  document.getElementById("check-sum-96").disabled = valor;
  document.getElementById("sum-96").disabled = valor;
  document.getElementById("check-sum-101").disabled = valor;
  document.getElementById("sum-101").disabled = valor;
}

// Procedimiento que limpia la prueba completa
function limpiarSuma(){
  suma = 1;
  aciertos = 0;
  errores = 0;
  num_ant = 1;
  document.getElementById("aciertos-suma").innerHTML = 0;
  document.getElementById("errores-suma").innerHTML = 0;

  document.getElementById("check-sum-6").checked = false;
  document.getElementById("sum-6").value = "";
  document.getElementById("check-sum-11").checked = false;
  document.getElementById("sum-11").value = "";
  document.getElementById("check-sum-16").checked = false;
  document.getElementById("sum-16").value = "";
  document.getElementById("check-sum-21").checked = false;
  document.getElementById("sum-21").value = "";
  document.getElementById("check-sum-26").checked = false;
  document.getElementById("sum-26").value = "";
  document.getElementById("check-sum-31").checked = false;
  document.getElementById("sum-31").value = "";
  document.getElementById("check-sum-36").checked = false;
  document.getElementById("sum-36").value = "";
  document.getElementById("check-sum-41").checked = false;
  document.getElementById("sum-41").value = "";
  document.getElementById("check-sum-46").checked = false;
  document.getElementById("sum-46").value = "";
  document.getElementById("check-sum-51").checked = false;
  document.getElementById("sum-51").value = "";
  document.getElementById("check-sum-56").checked = false;
  document.getElementById("sum-56").value = "";
  document.getElementById("check-sum-61").checked = false;
  document.getElementById("sum-61").value = "";
  document.getElementById("check-sum-66").checked = false;
  document.getElementById("sum-66").value = "";
  document.getElementById("check-sum-71").checked = false;
  document.getElementById("sum-71").value = "";
  document.getElementById("check-sum-76").checked = false;
  document.getElementById("sum-76").value = "";
  document.getElementById("check-sum-81").checked = false;
  document.getElementById("sum-81").value = "";
  document.getElementById("check-sum-86").checked = false;
  document.getElementById("sum-86").value = "";
  document.getElementById("check-sum-91").checked = false;
  document.getElementById("sum-91").value = "";
  document.getElementById("check-sum-96").checked = false;
  document.getElementById("sum-96").value = "";
  document.getElementById("check-sum-101").checked = false;
  document.getElementById("sum-101").value = "";
}

// Procedimiento que inicia la resta
function iniciarResta() {
  click_resum.play();
  console.log("hola bebe")
  if(res_flag == 1){
    apagarPanel(1,false);
    num_ant = 40;
    control = setInterval(cronometroResta_1, 10);
    document.getElementById("resta_1-37").focus();
    if(parseInt(age) < 10){
      document.getElementById("progreso-resta").textContent ="1 / 1";
    }else{
      document.getElementById("progreso-resta").textContent ="1 / 2";
    }
  }else{
    apagarPanel(2,false);
    num_ant = 100;
    control = setInterval(cronometroResta_2, 10);
    document.getElementById("resta-93").focus();
  }

  document.getElementById("inicio_resta").disabled = true;
  document.getElementById("reiniciar_resta").disabled = false;
}

// Procedimiento que detiene la resta
function pararResta() {
  if(res_flag == 1){
    apagarPanel(1, true);
    if(parseInt(age) > 9){
      document.getElementById("siguiente_resta").disabled = false;
    }
    document.getElementById("reiniciar_resta").disabled = true;
  }else{
    apagarPanel(2, true);
    document.getElementById("reiniciar_resta").disabled = true;
  }
  clearInterval(control);
  res_flag = 2; 
}

// Procedimiento que muestra la siguiente resta
function siguienteResta(){
  click_resum.play();
  document.getElementById("progreso-resta").textContent ="2 / 2";
  document.getElementById("reloj-resta-1").className = "apagado";
  document.getElementById("resta-panel-1").className = "apagado";
  document.getElementById("reloj-resta-2").classList.remove("apagado");
  document.getElementById("resta-panel-2").classList.remove("apagado"); 
  document.getElementById("inicio_resta").disabled = false;
  document.getElementById("siguiente_resta").disabled = true;
  document.getElementById("resta-instruct-1").className = "apagado";
  document.getElementById("resta-instruct-2").classList.remove("apagado");
}

// Procedimiento que reinicia la resta
function reiniciarResta() {
  click_resum.play();
  clearInterval(control);
  limpiarResta();
  if(res_flag == 1){
    apagarPanel(1, true);
    centesimas = segundos = 0;
    document.getElementById("segundos_resta_1").innerHTML = "0";
  }else{ 
    apagarPanel(2, true);
    centesimas_2 = segundos_2 = 0;
    document.getElementById("segundos_resta_2").innerHTML = "0";
  }
  document.getElementById("inicio_resta").disabled = false;
  document.getElementById("reiniciar_resta").disabled = true;
}

// Procedimiento que funciona como cronometro de la resta A
function cronometroResta_1() {
  if (segundos == 300) {
    alarma.play();
    pararResta();
    document.getElementById("text-modal-res").textContent = "Tarea A finalizada";
    document.getElementById("box-modal-res").style.width = "20%";
    document.getElementById("modal-res").style.display = "block";
    document.getElementById("btnModal-res").onclick = function() {
      click_resum.play();
      document.getElementById("modal-res").style.display = "none";
    }
    
  }
  if (centesimas < 99) {
    centesimas++;
  }

  if (centesimas == 99) {
    centesimas = -1;
  }
  if (centesimas == 0) {
    segundos++;
    document.getElementById("segundos_resta_1").innerHTML = "" + segundos;
  }
}

// Procedimiento que funciona como cronometro de la resta B
function cronometroResta_2() {
  if (segundos_2 == 300) {
    alarma.play();
    pararResta();
    document.getElementById("text-modal-res").textContent = "Tarea B finalizada";
    document.getElementById("box-modal-res").style.width = "20%";
    document.getElementById("modal-res").style.display = "block";
    document.getElementById("btnModal-res").onclick = function() {
      click_resum.play();
      document.getElementById("modal-res").style.display = "none";
    }
    
  }
  if (centesimas_2 < 99) {
    centesimas_2++;
  }

  if (centesimas_2 == 99) {
    centesimas_2 = -1;
  }
  if (centesimas_2 == 0) {
    segundos_2++;
    console.log(segundos_2);
    document.getElementById("segundos_resta_2").innerHTML = "" + segundos_2;
  }
}

// Procedimiento que toma el valor dado en cada campo de texto
function presionarTecla_Resta(checkbox,textbox,text_sig){
  var text = document.getElementById(textbox).value;
  
  if (event.key == "Enter"){
    if(document.getElementById(checkbox).checked){
      if(text == null){
        resta[x] += num_ant;
      }else{
        resta[x] += num_ant;
      }
      if(result_ant == "acierto"){
        ac_resta[x] -= 1;
      }else if(result_ant == "error"){
        err_resta[x] -= 1;
      }
    }else{
      document.getElementById(checkbox).checked = true;
    }

    if(text_sig != null){
      document.getElementById(text_sig).focus();
    }
    
    validarResta(textbox,text_sig);
  }
}

// Procedimiento que asigna los resultados de BANFE a los valores en la página
function validarResta(textbox,text_sig){
  if(res_flag == 1){
    comprobarResta(3,0,textbox);
    document.getElementById("aciertos-resta-1").innerHTML = ac_resta[0];
    document.getElementById("errores-resta-1").innerHTML = err_resta[0];
  }else{
    x = 1;
    comprobarResta(7,1,textbox);
    document.getElementById("aciertos-resta-2").innerHTML = ac_resta[1];
    document.getElementById("errores-resta-2").innerHTML = err_resta[1];
  }

  if(text_sig == null){
    if(res_flag == 1){
      pararResta();
    }else{
      pararResta();
    }
  }
}

// Procedimiento que valida que el valor recibido sea correcto
function comprobarResta(num_res,x,textbox){
  text = document.getElementById(textbox).value;
  valor = document.getElementById(textbox).placeholder;

  if (text.length == 0) {
    if(parseInt(valor,10) == (resta[x]-num_res)){
        result_ant = "acierto";
        ac_resta[x] += 1;
        resta[x] -= num_res;
        x == 0 ? num_ant = 3 : num_ant == 7;
    }else{
        result_ant = "error";
        err_resta[x] += 1;
        num_ant = resta[x] - parseInt(valor,10);
        resta[x] = parseInt(valor,10);
    }
  }else{
    if(parseInt(text,10) == (resta[x]-num_res)){
      result_ant = "acierto";
      ac_resta[x] += 1;
      resta[x] -= num_res;
      x == 0 ? num_ant = 3 : num_ant == 7;
    }else{
      result_ant = "error";
      err_resta[x] += 1;
      num_ant = resta[x] - parseInt(text,10);
      resta[x] = parseInt(text,10);
    }
  }
}

// Procedimiento que inhabilita los campos de la resta correspondiente
function apagarPanel(panel,valor){
  if(panel == 1){
    document.getElementById("check-resta_1-37").disabled = valor;
    document.getElementById("resta_1-37").disabled = valor;
    document.getElementById("check-resta-34").disabled = valor;
    document.getElementById("resta-34").disabled = valor;
    document.getElementById("check-resta-31").disabled = valor;
    document.getElementById("resta-31").disabled = valor;
    document.getElementById("check-resta-28").disabled = valor;
    document.getElementById("resta-28").disabled = valor;
    document.getElementById("check-resta-25").disabled = valor;
    document.getElementById("resta-25").disabled = valor;
    document.getElementById("check-resta-22").disabled = valor;
    document.getElementById("resta-22").disabled = valor;
    document.getElementById("check-resta-19").disabled = valor;
    document.getElementById("resta-19").disabled = valor;
    document.getElementById("check-resta_1-16").disabled = valor;
    document.getElementById("resta_1-16").disabled = valor;   
    document.getElementById("check-resta-13").disabled = valor;
    document.getElementById("resta-13").disabled = valor; 
    document.getElementById("check-resta-10").disabled = valor;
    document.getElementById("resta-10").disabled = valor;
    document.getElementById("check-resta-7").disabled = valor;
    document.getElementById("resta-7").disabled = valor;
    document.getElementById("check-resta-4").disabled = valor;
    document.getElementById("resta-4").disabled = valor;
    document.getElementById("check-resta-1").disabled = valor;
    document.getElementById("resta-1").disabled = valor;
  }else if(panel == 2){
    document.getElementById("check-resta-93").disabled = valor;
    document.getElementById("resta-93").disabled = valor;
    document.getElementById("check-resta-86").disabled = valor;
    document.getElementById("resta-86").disabled = valor;
    document.getElementById("check-resta-79").disabled = valor;
    document.getElementById("resta-79").disabled = valor;
    document.getElementById("check-resta-72").disabled = valor;
    document.getElementById("resta-72").disabled = valor;
    document.getElementById("check-resta-65").disabled = valor;
    document.getElementById("resta-65").disabled = valor;
    document.getElementById("check-resta-58").disabled = valor;
    document.getElementById("resta-58").disabled = valor;
    document.getElementById("check-resta-51").disabled = valor;
    document.getElementById("resta-51").disabled = valor;
    document.getElementById("check-resta-44").disabled = valor;
    document.getElementById("resta-44").disabled = valor;
    document.getElementById("check-resta_2-37").disabled = valor;
    document.getElementById("resta_2-37").disabled = valor;
    document.getElementById("check-resta-30").disabled = valor;
    document.getElementById("resta-30").disabled = valor;
    document.getElementById("check-resta-23").disabled = valor;
    document.getElementById("resta-23").disabled = valor;
    document.getElementById("check-resta_2-16").disabled = valor;
    document.getElementById("resta_2-16").disabled = valor;
    document.getElementById("check-resta-9").disabled = valor;
    document.getElementById("resta-9").disabled = valor;
    document.getElementById("check-resta-2").disabled = valor;
    document.getElementById("resta-2").disabled = valor;
  }
}

// Procedimiento que limpia la resta correspondiente
function limpiarResta(){
  if(res_flag == 1){
    resta[0] = 40;
    ac_resta[0] = 0;
    err_resta[0] = 0;
    num_ant = 40;

    document.getElementById("aciertos-resta-1").innerHTML = 0;
    document.getElementById("errores-resta-1").innerHTML = 0;

    document.getElementById("check-resta_1-37").checked = false;
    document.getElementById("resta_1-37").value = "";
    document.getElementById("check-resta-34").checked = false;
    document.getElementById("resta-34").value = "";
    document.getElementById("check-resta-31").checked = false;
    document.getElementById("resta-31").value = "";
    document.getElementById("check-resta-28").checked = false;
    document.getElementById("resta-28").value = "";
    document.getElementById("check-resta-25").checked = false;
    document.getElementById("resta-25").value = "";
    document.getElementById("check-resta-22").checked = false;
    document.getElementById("resta-22").value = "";
    document.getElementById("check-resta-19").checked = false;
    document.getElementById("resta-19").value = "";
    document.getElementById("check-resta_1-16").checked = false;
    document.getElementById("resta_1-16").value = "";
    document.getElementById("check-resta-13").checked = false;
    document.getElementById("resta-13").value = "";
    document.getElementById("check-resta-10").checked = false;
    document.getElementById("resta-10").value = "";
    document.getElementById("check-resta-7").checked = false;
    document.getElementById("resta-7").value = "";
    document.getElementById("check-resta-4").checked = false;
    document.getElementById("resta-4").value = "";
    document.getElementById("check-resta-1").checked = false;
    document.getElementById("resta-1").value = "";
  }else{
    resta[1] = 40;
    ac_resta[1] = 0;
    err_resta[1] = 0;
    num_ant = 100;

    document.getElementById("aciertos-resta-2").innerHTML = 0;
    document.getElementById("errores-resta-2").innerHTML = 0;

    document.getElementById("check-resta-93").checked = false;
    document.getElementById("resta-93").value = "";
    document.getElementById("check-resta-86").checked = false;
    document.getElementById("resta-86").value = "";
    document.getElementById("check-resta-79").checked = false;
    document.getElementById("resta-79").value = "";
    document.getElementById("check-resta-72").checked = false;
    document.getElementById("resta-72").value = "";
    document.getElementById("check-resta-65").checked = false;
    document.getElementById("resta-65").value = "";
    document.getElementById("check-resta-58").checked = false;
    document.getElementById("resta-58").value = "";
    document.getElementById("check-resta-51").checked = false;
    document.getElementById("resta-51").value = "";
    document.getElementById("check-resta-44").checked = false;
    document.getElementById("resta-44").value = "";
    document.getElementById("check-resta_2-37").checked = false;
    document.getElementById("resta_2-37").value = "";
    document.getElementById("check-resta-30").checked = false;
    document.getElementById("resta-30").value = "";
    document.getElementById("check-resta-23").checked = false;
    document.getElementById("resta-23").value = "";
    document.getElementById("check-resta_2-16").checked = false;
    document.getElementById("resta_2-16").value = "";
    document.getElementById("check-resta-9").checked = false;
    document.getElementById("resta-9").value = "";
    document.getElementById("check-resta-2").checked = false;
    document.getElementById("resta-2").value = "";
  }
}