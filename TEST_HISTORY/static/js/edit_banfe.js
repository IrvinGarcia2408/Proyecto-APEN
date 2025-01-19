// Función para manejar el incremento en los valores
function add(amount, category) {
  var hiddenInput;
  const totalElement = document.getElementById(`total-${category}`);
  let currentValue = parseInt(totalElement.innerText);

  currentValue += amount;
  totalElement.innerText = currentValue;

  if (category != 'specific_animals' && category != 'functional_animals' && category != 'abstract_animals'){
    console.log("No es promedio")
    hiddenInput = document.querySelector('input[name="' + category + '"]');
    console.log(category)
    hiddenInput.value = currentValue;
  }

  // Habilitar el botón de resta si el valor es mayor que 0
  document.getElementById(`res-${category}`).disabled =
    currentValue <= 0 ? true : false;

  if (
    category === "specific_categories" ||
    category === "specific_animals" ||
    category === "functional_categories" ||
    category === "functional_animals" ||
    category === "abstract_categories" ||
    category === "abstract_animals"
  ) {
    updateSemantics();
  }
}

// Función para manejar el decremento en los valores
function substract(amount, category) {
  const totalElement = document.getElementById(`total-${category}`);
  var hiddenInput;
  let currentValue = parseInt(totalElement.innerText);

  currentValue -= amount;
  currentValue = Math.max(currentValue, 0);
  totalElement.innerText = currentValue;

  if (category != 'specific_animals' && category != 'functional_animals' && category != 'abstract_animals'){
    console.log("No es promedio")
    hiddenInput = document.querySelector('input[name="' + category + '"]');
    console.log(category)
    hiddenInput.value = currentValue;
  }

  // Deshabilitar el botón de decremento si el valor es 0
  document.getElementById(`res-${category}`).disabled =
    currentValue <= 0 ? true : false;

  if (
    category === "specific_categories" ||
    category === "specific_animals" ||
    category === "functional_categories" ||
    category === "functional_animals" ||
    category === "abstract_categories" ||
    category === "abstract_animals"
  ) {
    updateSemantics();
  }
}

// Función para actualizar el total y el promedio para semanticas
function updateSemantics() {
  let elementAverage = [0, 0, 0];
  let totalAverage = 0;
  const specificCategories = parseInt(
    document.getElementById("total-specific_categories").innerText
  );
  const specificAnimals = parseInt(
    document.getElementById("total-specific_animals").innerText
  );
  const functionalCategories = parseInt(
    document.getElementById("total-functional_categories").innerText
  );
  const functionalAnimals = parseInt(
    document.getElementById("total-functional_animals").innerText
  );
  const abstractCategories = parseInt(
    document.getElementById("total-abstract_categories").innerText
  );
  const abstractAnimals = parseInt(
    document.getElementById("total-abstract_animals").innerText
  );

  const totalCategories =
    specificCategories + functionalCategories + abstractCategories;
  console.log("Categorías: "+totalCategories)
  const totalAnimals = specificAnimals + functionalAnimals + abstractAnimals;
  console.log("Animales: "+totalAnimals)

  // Evitar la división por cero
  elementAverage[0] = specificCategories === 0 ? 0 : specificAnimals / specificCategories;
  elementAverage[1] = functionalCategories === 0 ? 0 : functionalAnimals / functionalCategories;
  elementAverage[2] = abstractCategories === 0 ? 0 : abstractAnimals / abstractCategories;


  totalAverage = truncar(totalAnimals / totalCategories, 0);
  let totalScore =
    specificAnimals + functionalAnimals * 2 + abstractAnimals * 3;

  // Si totalAverage es NaN o Infinity, asignar 0
  if (isNaN(totalAverage) || !isFinite(totalAverage)) {
    totalAverage = 0;
  }

  // Actualizar los campos de texto
  document.getElementById("total-average").innerText = totalAverage;
  document.getElementById("total-score").innerText = totalScore;

  // Actualizar los campos ocultos
  document.querySelector('input[name="specific_average"]').value = elementAverage[0];
  document.querySelector('input[name="functional_average"]').value = elementAverage[1];
  document.querySelector('input[name="abstract_average"]').value = elementAverage[2];
  document.querySelector('input[name="total_categories"]').value = totalCategories;
  document.querySelector('input[name="total_average"]').value = totalAverage;
  document.querySelector('input[name="total_score"]').value = totalScore;
}

// Función que trunca un número al número específico de decimales proporcionado
function truncar(numero, decimales) {
  // Calcula el factor de escala para truncar el número
  const factor = Math.pow(10, decimales);

  // Multiplica el número por el factor de escala, trunca el resultado y divide nuevamente por el factor para obtener el número truncado
  return Math.trunc(numero * factor) / factor;
}

// Inicializar el estadoo de los botones de decremento
document.addEventListener("DOMContentLoaded", () => {
  const categories = [
    "touch",
    "cross",
    "caught",
    "specific_categories",
    "specific_animals",
    "functional_categories",
    "functional_animals",
    "abstract_categories",
    "abstract_animals",
    "successes",
    "intrusions",
    "perseverations",
  ];

  categories.forEach((category) => {
    const totalElement = document.getElementById(`total-${category}`);
    const currentValue = parseInt(totalElement.innerText);
    console.log(category)
    document.getElementById(`res-${category}`).disabled =
      currentValue <= 0 ? true : false;
  });

  updateSemantics();
});
