let click_semanticas = document.querySelector(".figure-sound");
let categories = [0, 0, 0];
let addElements = [0, 0, 0];
let elementAverage = [0, 0, 0];

let sec_semantics = 0;
let cen_semantics = 0;

// Variables para almacenar el estado anterior de los radios
let previousClasify = createEmptyArray(20);
let previousAmount = createEmptyArray(20);

// Función para crear una lista con valores nulos de una dimensión dada
function createEmptyArray(length) {
  // Inicializar un array vacío
  const array = [];

  // Iterar sobre la longitud especificada
  for (let i = 0; i < length; i++) {
    // Agregar un valor nulo al array en cada iteración
    array.push(null);
  }

  // Devolver el array creado
  return array;
}


// Procedimiento que inicia la prueba del lado del sujeto
function iniciarSemanticas() {
  document.getElementById("text-modal-sem").textContent =
    "La siguiente tarea consiste en que clasifique las figuras que ve en lámina que aparece en la pantalla; usted me dirá el criterio por el que las está clasificando y cuáles figuras pertenecen al grupo elegido. Puede volver a mencionar diversas figuras en clasificaciones diferentes. Haga la mayor cantidad posible de agrupaciones. Yo le indicaré cuando termine su tiempo.";
  document.getElementById("box-modal-sem").style.width = "40%";
  document.getElementById("modal-sem").style.display = "block";

  document.getElementById("btnModal-sem").onclick = function () {
    click_semanticas.play();
    document.getElementById("modal-sem").style.display = "none";
    if (
      document.getElementById("text-modal-sem").textContent !=
      "Prueba finalizada"
    ) {
      control = setInterval(relojSemanticas, 10);
    }
  };
}

// Función que filtra solo números en un campo de texto
function onlyNumbers(evt) {
  let code = evt.which ? evt.which : evt.keyCode;

  if (code == 8) {
    // backspace
    return true;
  } else if (code >= 48 && code <= 57) {
    //is an numer
    return true;
  } else {
    //other keys
    return false;
  }
}

// Procedimiento que recibe la cantidad de figuras por categoria
function checkCategorySelection(category, textbox) {
  cant = document.getElementById(textbox).value;

  if (event.key == "Enter") {
    if (cant == "") {
      deleteAmount(category)
      document.getElementById("text-modal-sem").textContent = "Campo vacío";
      document.getElementById("box-modal-sem").style.width = "20%";
      document.getElementById("modal-sem").style.display = "block";

      document.getElementById("btnModal-sem").onclick = function () {
        click_semanticas.play();
        document.getElementById("modal-sem").style.display = "none";
      };
    } else {
      if (!isRadioButtonsSelected(category)) {
        document.getElementById("text-modal-sem").textContent =
          "Debes seleccionar una categoría antes de ingresar la cantidad";
        document.getElementById("box-modal-sem").style.width = "30%";
        document.getElementById("modal-sem").style.display = "block";

        document.getElementById("btnModal-sem").onclick = function () {
          click_semanticas.play();
          document.getElementById("modal-sem").style.display = "none";
        };
      } else {
        deleteAmount(category)
        addAmount(category, parseInt(cant))
        document.getElementById("text-modal-sem").textContent =
          "Categoría actualizada";
        document.getElementById("box-modal-sem").style.width = "20%";
        document.getElementById("modal-sem").style.display = "block";

        document.getElementById("btnModal-sem").onclick = function () {
          click_semanticas.play();
          document.getElementById("modal-sem").style.display = "none";
        };
      }
    }
  }
}

function isRadioButtonsSelected(groupname) {
  // Obtener todos los elementos de radio con el mismo nombre
  var radios = document.getElementsByName("sem_" + groupname);

  // Iterar sobre los radios
  for (var i = 0; i < radios.length; i++) {
    // Verificar si el radio actual está seleccionado
    if (radios[i].checked) {
      // Si uno está seleccionado, retorna verdadero
      return true;
    }
  }

  // Si ninguno está seleccionado, retorna falso
  return false;
}

function addAmount(category, amount) {
  if (previousClasify[category-1] === 'C'){
    addElements[0] += amount;
    previousAmount[category-1] = amount;
    elementAverage[0] = addElements[0]/categories[0];
  } else if (previousClasify[category-1] === 'F'){
    addElements[1] += amount;
    previousAmount[category-1] = amount;
    elementAverage[1] = addElements[1]/categories[1];
  } else if (previousClasify[category-1] === 'A') {
    addElements[2] += amount;
    previousAmount[category-1] = amount;
    elementAverage[2] = addElements[2]/categories[2];
  }
}

function deleteAmount(category) {
  if (previousClasify[category-1] === 'C'){
    addElements[0] -= previousAmount[category-1];
    previousAmount[category-1] = null;
    elementAverage[0] = addElements[0]/categories[0];
  } else if (previousClasify[category-1] === 'F'){
    alert(category+" | "+addElements[1])
    addElements[1] -= previousAmount[category-1];
    previousAmount[category-1] = null;
    elementAverage[1] = addElements[1]/categories[1];
    alert(category+" | "+addElements[1])
  } else if (previousClasify[category-1] === 'A') {
    addElements[2] -= previousAmount[category-1];
    previousAmount[category-1] = null;
    elementAverage[2] = addElements[2]/categories[2];    
  }
}


function addCategory(category) {
  if (previousClasify[category-1] === 'C'){
    categories[0] += 1;
  } else if (previousClasify[category-1] === 'F'){
    categories[1] += 1;
  } else if (previousClasify[category-1] === 'A') {
    categories[2] += 1;
  }
}

function deleteCategory(category) {
  if (previousClasify[category-1] === 'C'){
    categories[0] -= 1;
  } else if (previousClasify[category-1] === 'F'){
    categories[1] -= 1;
  } else if (previousClasify[category-1] === 'A') {
    categories[2] -= 1;
  }
}

// Función para manejar el cambio en la selección de los radios
function handleRadioChange(category, clasify, radioButton) {
  // Verificar si ya se había seleccionado una clasificación para esta categoría
  if (previousClasify[category-1] !== null) {
    // Deshacer la selección anterior (deseleccionar el radio previamente seleccionado)
    if (previousClasify[category-1] === clasify) {
      document.getElementById(radioButton).checked = false;  
      deleteCategory(category);
      deleteAmount(category);
      previousClasify[category-1] = null;
    } else {
      // Almacenar la nueva clasificación seleccionada 
      deleteCategory(category)
      deleteAmount(category);
      previousClasify[category-1] = clasify;
      addCategory(category)
    }
    document.getElementById("total_"+category).value = "";
    alert("deseleccionamos y volvemos a seleccionar");
  } else {
    // Almacenar la clasificación seleccionada
    previousClasify[category-1] = clasify;
    addCategory(category);

    alert("seleccionamos");
  }
}


// Procedimiento que muestra los datos BANFE actualizados
function mostrarSemanticas() {
  let dividendo = addElements[0] + addElements[1] + addElements[2];
  let divisor = categories[0] + categories[1] + categories[2];
  let totalAverage = truncar(dividendo/divisor,0);

  console.log("dividendo: "+dividendo)
  console.log("divisor: "+divisor)
  console.log("resultado: "+truncar(totalAverage,0))

  document.getElementById("total-cat").textContent =
    categories[0] + categories[1] + categories[2];
  document.getElementById("total-concretas").textContent = categories[0];
  document.getElementById("total-funcionales").textContent = categories[1];
  document.getElementById("total-abstractas").textContent = categories[2];
  document.getElementById("puntos-finales").textContent =
    categories[0] + categories[1] * 2 + categories[2] * 3;
  if (totalAverage > 0) {
    document.getElementById("total-prom").textContent = totalAverage;
  } else {
    document.getElementById("total-prom").textContent = 0;
  }
}

// Función que trunca un número al número específico de decimales proporcionado
function truncar(numero, decimales) {
  // Calcula el factor de escala para truncar el número
  const factor = Math.pow(10, decimales);
  
  // Multiplica el número por el factor de escala, trunca el resultado y divide nuevamente por el factor para obtener el número truncado
  return Math.trunc(numero * factor) / factor;
}


// Procedimiento que inicia el cronometro del lado del sujeto
function relojSemanticas() {
  if (sec_semantics == 300) {
    clearInterval(control);
    document.getElementById("text-modal-sem").textContent = "Prueba finalizada";
    document.getElementById("box-modal-sem").style.width = "20%";
    document.getElementById("modal-sem").style.display = "block";
  }
  console.log(
    "Segundos: " + sec_semantics + " | Centesimas: " + cen_semantics
  );
  if (cen_semantics < 99) {
    cen_semantics++;
  }

  if (cen_semantics == 99) {
    cen_semantics = -1;
  }
  if (cen_semantics == 0) {
    sec_semantics++;
  }
}
