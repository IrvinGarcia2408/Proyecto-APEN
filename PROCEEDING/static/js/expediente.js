const proceedingForm = document.getElementById("form-proceeding");
const updateForm = document.getElementById("update-proceeding");

const inputs = document.querySelectorAll('#form-proceeding input[type="text"]');
const updateInputs = document.querySelectorAll('#update-proceeding input[type="text"]');

const checkboxs = document.querySelectorAll(
  '#form-proceeding input[type="checkbox"]'
);
const updateCheckboxs = document.querySelectorAll(
  '#update-proceeding input[type="checkbox"]'
);

const selects = document.querySelectorAll("#form-proceeding select");
const updateSelects = document.querySelectorAll("#update-proceeding select");

const dateInputs = document.querySelectorAll(
  '#form-proceeding input[type="date"]'
);

const dateUpdateInputs = document.querySelectorAll(
  '#update-proceeding input[type="date"]'
);

const expressions = {
  words: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos
  word: /^[a-zA-ZÀ-ÿ]{1,30}$/, // Letras, pueden llevar acentos
  texts: /^[a-zA-ZÀ-ÿ0-9\s\.,]{1,60}$/, // Letras y espacios, pueden llevar acentos, puntos y comas
  paragraphs: /^[a-zA-ZÀ-ÿ,;:\-\s\.\(\)]{1,400}$/, // Texto sin caracteres especiales
  list: /^[A-Za-zÀ-ÿ,\s]{1,50}$/, // Letras separadas por comas
  listspecial: /^[A-Za-zÀ-ÿ0-9,\-]{1,50}$/, // Letras separadas por comas
  phone: /^\d{7,14}$/, // 7 a 14 números
  numbers: /^\d{1,2}$/, // 1 o 2 números
};

const fields = {
  name: false,
  flastName: false,
  slastName: false,
  dateEval: false,
  dateNac: false,
  country: false,
  state: false,
  municipality: false,
  language: false,
  indigenous_language: false,
  talk_other_language: true,
  gender: false,
  scholarship: false,
  years_study: false,
  laterality: false,
  occupation: false,
  instrument: false,
  time_instrument: false,
  hobbies: false,
  time_hobbies: false,
  civil_status: false,
  religion: false,
  mother_scholarship: false,
  father_scholarship: false,
  referred_by: false,
  phone_number: false,
  reason_consultation: false,
  alert_status: false,
  medicine: false,
  other_exams: false,
  hypertension: true,
  pulmonary_diseases: true,
  alcoholism: true,
  drugs: true,
  decrease_senses: true,
  craniocerebral_trauma: true,
  diabetes: true,
  hypothyroidsm: true,
  strokes: true,
  others_diseases: true,
};

const updateFields = {
  name: true,
  flastName: true,
  slastName: true,
  dateEval: true,
  dateNac: true,
  country: true,
  state: true,
  municipality: true,
  language: true,
  indigenous_language: true,
  talk_other_language: true,
  gender: true,
  scholarship: true,
  years_study: true,
  laterality: true,
  occupation: true,
  instrument: true,
  time_instrument: true,
  hobbies: true,
  time_hobbies: true,
  civil_status: true,
  religion: true,
  mother_scholarship: true,
  father_scholarship: true,
  referred_by: true,
  phone_number: true,
  reason_consultation: true,
  alert_status: true,
  medicine: true,
  other_exams: true,
  hypertension: true,
  pulmonary_diseases: true,
  alcoholism: true,
  drugs: true,
  decrease_senses: true,
  craniocerebral_trauma: true,
  diabetes: true,
  hypothyroidsm: true,
  strokes: true,
  others_diseases: true,
};


// Validación de los campos del formulario
const validateForm = (e) => {
  switch (e.target.name) {
    case "name":
      validateField(expressions.words, e.target, "name");
      document.getElementById("name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "first_last_name":
      validateField(expressions.word, e.target, "flastName");
      document.getElementById("first_last_name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "second_last_name":
      validateField(expressions.word, e.target, "slastName");
      document.getElementById("second_last_name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "dateEval":
      putRange(e.target), validateDate(e.target, "dateEval");
      break;
    case "dateNac":
      putRange(e.target), validateDate(e.target, "dateNac");
      break;
    case "language":
      validateField(expressions.word, e.target, "language");
      document.getElementById("language").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "indigenous_language":
      validateField(expressions.word, e.target, "indigenous_language");
      document.getElementById("indigenous_language").value =
        capitalizeFirstLetter(e.target.value);
      break;
    case "other_languages":
      validateField(expressions.list, e.target, "talk_other_language");
      document.getElementById("other_languages").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "scholarship":
      validateField(expressions.word, e.target, "scholarship");
      document.getElementById("scholarship").value = capitalizeFirstWord(
        e.target.value
      );
      break;
    case "years_study":
      validateField(expressions.numbers, e.target, "scholarship");
      break;
    case "occupation":
      validateField(expressions.words, e.target, "occupation");
      document.getElementById("occupation").value = capitalizeFirstWord(
        e.target.value
      );
      break;
    case "mother_scholarship":
      validateField(expressions.word, e.target, "mother_scholarship");
      document.getElementById("mother_scholarship").value = capitalizeFirstWord(
        e.target.value
      );
      break;
    case "father_scholarship":
      validateField(expressions.word, e.target, "father_scholarship");
      document.getElementById("father_scholarship").value = capitalizeFirstWord(
        e.target.value
      );
      break;
    case "referred_by":
      validateField(expressions.texts, e.target, "referred_by");
      document.getElementById("referred_by").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "phone_number":
      validateField(expressions.phone, e.target, "phone_number");
      break;
    case "reason_consultation":
      validateField(expressions.texts, e.target, "reason_consultation");
      document.getElementById("reason_consultation").value =
        capitalizeFirstWord(e.target.value);
      break;
    case "alert_status":
      validateField(expressions.texts, e.target, "alert_status");
      document.getElementById("alert_status").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "medicine":
      validateField(expressions.texts, e.target, "medicine");
      document.getElementById("medicine").value = capitalizeFirstWord(
        e.target.value
      );
      break;
    case "other_exams":
      validateField(expressions.texts, e.target, "other_exams");
      document.getElementById("other_exams").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "details_others_diseases":
      validateField(expressions.listspecial, e.target, "others_diseases");
      document.getElementById("diseases_input").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
  }
};

//  Validación de cada campo tipo text
const validateField = (expression, input, field) => {
  input.required = true;
  if (expression.test(input.value)) {
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.remove("form__input-error-active");
    if (input.name == "years_study") {
      fields["years_study"] = true;
      updateFields["years_study"] = true;
    } else {
      fields[field] = true;
      updateFields[field] = true;
    }
  } else {
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.add("form__input-error-active");
    if (input.name == "years_study") {
      fields["years_study"] = false;
      updateFields["years_study"] = false;
    } else {
      fields[field] = false;
      updateFields[field] = false;
    }
  }
};

// Asignación de eventos a los input=text
inputs.forEach((input) => {
  input.addEventListener("keyup", validateForm);
  input.addEventListener("blur", validateForm);
});

// Asignación de eventos a los input=text
updateInputs.forEach((input) => {
  input.addEventListener("keyup", validateForm);
  input.addEventListener("blur", validateForm);
});

// Validación de los select del formulario
const validateSelects = (e) => {
  switch (e.target.name) {
    case "gender":
      validateOption(e.target, "gender");
      break;
    case "laterality":
      validateOption(e.target, "laterality");
      break;
    case "time_instrument":
      validateOption(e.target, "time_instrument");
      break;
    case "time_hobbies":
      validateOption(e.target, "time_hobbies");
      break;
    case "civil_status":
      validateOption(e.target, "civil_status");
      break;
    case "religion":
      validateOption(e.target, "religion");
      break;
    case "time_hyperthension":
      validateOption(e.target, "hypertension");
      break;
    case "time_pulmonary_diseases":
      validateOption(e.target, "pulmonary_diseases");
      break;
    case "time_alcoholism":
      validateOption(e.target, "alcoholism");
      break;
    case "time_drugs":
      validateOption(e.target, "drugs");
      break;
    case "time_decrease_senses":
      validateOption(e.target, "decrease_senses");
      break;
    case "time_craniocerebral_trauma":
      validateOption(e.target, "craniocerebral_trauma");
      break;
    case "time_diabetes":
      validateOption(e.target, "diabetes");
      break;
    case "time_hypothyroidism":
      validateOption(e.target, "hypothyroidism");
      break;
    case "time_strokes":
      validateOption(e.target, "strokes");
      break;
  }
};

// Validación de cada option en el select
const validateOption = (select, field) => {
  select.required = true;
  if (select.value == "") {
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.add("form__input-error-active");
    fields[field] = false;
    updateFields[field] = false;
  } else {
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.remove("form__input-error-active");
    fields[field] = true;
    updateFields[field] = true;
  }
};

// Asignación de eventos a los select
selects.forEach((select) => {
  select.addEventListener("change", validateSelects);
  select.addEventListener("keyup", validateSelects);
  select.addEventListener("blur", validateSelects);
});

updateSelects.forEach((select) => {
  select.addEventListener("change", validateSelects);
  select.addEventListener("keyup", validateSelects);
  select.addEventListener("blur", validateSelects);
});

// Validación de los checkbox del formulario
const validateChecks = (e) => {
  switch (e.target.name) {
    case "talk_other_language":
      validateCheck(
        e.target,
        "input",
        "other_languages",
        "talk_other_language"
      );
      break;
    case "hyperthension":
      validateCheck(e.target, "combo", "time_hyperthension", "hypertension");
      break;
    case "pulmonary_diseases":
      validateCheck(
        e.target,
        "combo",
        "time_pulmonary_diseases",
        "pulmonary_diseases"
      );
      break;
    case "alcoholism":
      validateCheck(e.target, "combo", "time_alcoholism", "alcoholism");
      break;
    case "drugs":
      validateCheck(e.target, "combo", "time_drugs", "drugs");
      break;
    case "decrease_senses":
      validateCheck(
        e.target,
        "combo",
        "time_decrease_senses",
        "decrease_senses"
      );
      break;
    case "craniocerebral_trauma":
      validateCheck(
        e.target,
        "combo",
        "time_craniocerebral_trauma",
        "craniocerebral_trauma"
      );
      break;
    case "diabetes":
      validateCheck(e.target, "combo", "time_diabetes", "diabetes");
      break;
    case "hypothyroidism":
      validateCheck(e.target, "combo", "time_hypothyroidism", "hypothyroidsm");
      break;
    case "strokes":
      validateCheck(e.target, "combo", "time_strokes", "strokes");
      break;
    case "others_diseases":
      validateCheck(
        e.target,
        "input",
        "details_others_diseases",
        "others_diseases"
      );
      break;
  }
};

// Validación de los checks que habilitan otros elementos
const validateCheck = (check, element, name, field) => {
  if (check.checked) {
    fields[field] = false;
    updateFields[field] = false;

    document.getElementById(name).disabled = false;
    document.getElementById(name).required = true;
  } else {
    alert (fields[name])
    fields[field] = true;
    updateFields[field] = true;

    if (element != "combo") {
      document.getElementById(name).value = "";
    } else {
      document.getElementById(name).selectedIndex = 0;
    }
    document.getElementById(name).required = false;
    document.getElementById(name).disabled = true;

    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.remove("form__input-error-active");
  }
};

// Asignación del evento a los checkbox
checkboxs.forEach((checkbox) => {
  checkbox.addEventListener("change", validateChecks);
});

updateCheckboxs.forEach((checkbox) => {
  checkbox.addEventListener("change", validateChecks);
});

//  Procedimiento que asigna a los input=date un rango permitido de fechas
const putRange = (input) => {
  if (input.name == "dateEval") {
    document.getElementById(input.name).setAttribute("min", "2024-01-01"); // Fecha mínima: 1 de enero de 2024
  } else {
    document.getElementById(input.name).setAttribute("min", "1900-01-01"); // Fecha mínima: 1 de enero de 1900
  }
  document.getElementById(input.name).setAttribute("max", "3000-12-31"); // Fecha máxima: 31 de diciembre de 3000
};

//  Procedimiento que valida que los datos en los date sean válidos
const validateDate = (input, field) => {
  input.required = true;
  if (
    input.value <= document.getElementById(input.name).getAttribute("max") &&
    input.value >= document.getElementById(input.name).getAttribute("min")
  ) {
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.remove("form__input-error-active");
    fields[field] = true;
    updateFields[field] = true;
    if (input.name == "dateNac") {
      if (document.getElementById("edad").value < 6) {
        document
          .getElementById(`group__${field}`)
          .classList.add("form__group-incorrect");
        document
          .getElementById(`group__${field}`)
          .classList.remove("form__group-correct");
        document
          .querySelector(`#group__${field} .form__input-error`)
          .classList.add("form__input-error-active");
        fields[field] = false;
        updateFields[field] = false;
      }
    }
  } else {
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.add("form__input-error-active");
    fields[field] = false;
    updateFields[field] = false;
  }
};

//  Asignación de los eventos a los input=date
dateInputs.forEach((date) => {
  date.addEventListener("focus", validateForm);
  date.addEventListener("change", validateForm);
  date.addEventListener("blur", validateForm);
});

dateUpdateInputs.forEach((date) => {
  date.addEventListener("focus", validateForm);
  date.addEventListener("change", validateForm);
  date.addEventListener("blur", validateForm);
});

//  Procedimiento que invoca los estados pertenecientes a cada país
document.getElementById("country").addEventListener("change", function () {
  var countryId = this.value;
  this.required  = true;
  var xhr = new XMLHttpRequest();
  if (
    countryId != "" &&
    document.getElementById("country").options[countryId].textContent != "Otro"
  ) {
    document.getElementById("state").required = true;
    document.getElementById("municipality").required = true;
    fields["country"] = true;
    updateFields["country"] = true;
    xhr.open("GET", "/expedientes/crear/estados/?country=" + countryId, true);
    xhr.onload = function () {
      if (this.status === 200) {
        var states = JSON.parse(this.responseText);
        var stateSelect = document.getElementById("state");

        // borrar opciones anteriores
        while (stateSelect.options.length) {
          stateSelect.remove(0);
        }

        const selectEmpty = document.createElement("option");
        selectEmpty.value = "";
        selectEmpty.innerHTML = "Seleccione estado";
        stateSelect.appendChild(selectEmpty);
        document.getElementById("state").disabled = false;

        // agregar opciones de estados
        for (var state in states) {
          if (states.hasOwnProperty(state)) {
            var option = document.createElement("option");
            option.value = states[state].id;
            option.text = states[state].name;
            stateSelect.appendChild(option);
          }
        }
        document.getElementById("state").setAttribute("required", "true");

        // actualizar municipios
        if (document.getElementById("state").value != "") {
          document.getElementById("state").dispatchEvent(new Event("change"));
        } else {
          while (document.getElementById("municipality").options.length) {
            document.getElementById("municipality").remove(0);
          }
          const selectEmpty = document.createElement("option");
          selectEmpty.value = "";
          selectEmpty.innerHTML = "Seleccione municipio";
          document.getElementById("municipality").appendChild(selectEmpty);
          document.getElementById("municipality").disabled = false;
        }
      }
    };
    xhr.send();
  } else {
    document.getElementById("state").required = false;
    document.getElementById("municipality").required = false;
    fields["country"] = fields["state"] = fields["municipality"] = true;
    updateFields["country"] = updateFields["state"] = updateFields["municipality"] = true;
    const selectEmpty1 = document.createElement("option");

    while (document.getElementById("state").options.length) {
      document.getElementById("state").remove(0);
    }
    selectEmpty1.value = "";
    selectEmpty1.innerHTML = "Seleccione estado";
    document.getElementById("state").appendChild(selectEmpty1);
    document.getElementById("state").disabled = true;

    const selectEmpty2 = document.createElement("option");

    while (document.getElementById("municipality").options.length) {
      document.getElementById("municipality").remove(0);
    }
    selectEmpty2.value = "";
    selectEmpty2.innerHTML = "Seleccione municipio";
    document.getElementById("municipality").appendChild(selectEmpty2);
    document.getElementById("municipality").disabled = true;
  }
});

//  Procedimiento que invoca los municipios del estado que se seleccionó
document.getElementById("state").addEventListener("change", function () {
  var stateId = this.value;
  var xhr = new XMLHttpRequest();
  if (stateId != "") {
    fields["state"] = true;
    updateFields["state"] = true;
    xhr.open("GET", "/expedientes/crear/municipios/?state=" + stateId, true);
    xhr.onload = function () {
      if (this.status === 200) {
        var municipalities = JSON.parse(this.responseText);
        var municipalitiesSelect = document.getElementById("municipality");

        // borrar opciones anteriores
        while (municipalitiesSelect.options.length) {
          municipalitiesSelect.remove(0);
        }
        const selectEmpty = document.createElement("option");
        selectEmpty.value = "";
        selectEmpty.innerHTML = "Seleccione municipio";
        municipalitiesSelect.appendChild(selectEmpty);

        // agregar opciones de municipios
        if (municipalities != "") {
          for (var municipality in municipalities) {
            if (municipalities.hasOwnProperty(municipality)) {
              var option = document.createElement("option");
              option.value = municipalities[municipality].id;
              option.text = municipalities[municipality].name;
              municipalitiesSelect.appendChild(option);
            }
          }
        }
        document
          .getElementById("municipality")
          .setAttribute("required", "true");
      }
    };
    xhr.send();
  } else {
    fields["state"] = fields["municipality"] = true;
    updateFields["state"] = updateFields["municipality"] = true;
    while (document.getElementById("municipality").options.length) {
      document.getElementById("municipality").remove(0);
    }

    const selectEmpty = document.createElement("option");
    selectEmpty.value = "";
    selectEmpty.innerHTML = "Seleccione municipio";
    document.getElementById("municipality").appendChild(selectEmpty);
  }
});

//  Validación de que municipios no este vacío en caso de existir municipios
document.getElementById("municipality").addEventListener("change", function () {
  var municipalityId = this.value;
  if (municipalityId != "") {
    fields["municipality"] = true;
    updateFields["municipality"] = true;
  }
});

//  Validación de que si elige instrumentos habilite el tiempo que lo ha practicado
document.getElementById("instrument").addEventListener("change", function () {
  let timeSelect = document.getElementById("time_instrument");
  let instrumentSelect = document.getElementById("instrument");

  if (instrumentSelect.value != "") {
    document
      .getElementById(`group__instrument`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__instrument`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__instrument .form__input-error`)
      .classList.remove("form__input-error-active");
    timeSelect.getElementsByTagName("option")[0].selected = true;
    timeSelect.disabled = false;
    fields["instrument"] = true;
    fields["time_instrument"] = false;
    updateFields["instrument"] = true;
    updateFields["time_instrument"] = false;
    if (instrumentSelect.value == "Ninguno") {
      document
        .getElementById(`group__time_instrument`)
        .classList.remove("form__group-incorrect");
      document
        .getElementById(`group__time_instrument`)
        .classList.add("form__group-correct");
      document
        .querySelector(`#group__time_instrument .form__input-error`)
        .classList.remove("form__input-error-active");
      timeSelect.disabled = true;
      fields["time_instrument"] = true;
      updateFields["time_instrument"] = true;
    }
  } else {
    document
      .getElementById(`group__instrument`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__instrument`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__instrument .form__input-error`)
      .classList.add("form__input-error-active");
    fields["instrument"] = false;
    updateFields["instrument"] = false;
    timeSelect.getElementsByTagName("option")[0].selected = true;
    timeSelect.disabled = true;

    document
      .getElementById(`group__time_instrument`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__time_instrument`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__time_instrument .form__input-error`)
      .classList.remove("form__input-error-active");
  }
});

//  Validación de que si elige pasatiempos habilite la frecuencia con lo que lo hace
document.getElementById("hobbies").addEventListener("change", function () {
  let timeSelect = document.getElementById("time_hobbies");
  let hobbiesSelect = document.getElementById("hobbies");

  if (hobbiesSelect.value != "") {
    document
      .getElementById(`group__hobbies`)
      .classList.remove("form__group-incorrect");
    document
      .getElementById(`group__hobbies`)
      .classList.add("form__group-correct");
    document
      .querySelector(`#group__hobbies .form__input-error`)
      .classList.remove("form__input-error-active");
    timeSelect.getElementsByTagName("option")[0].selected = true;
    timeSelect.disabled = false;
    fields["hobbies"] = true;
    fields["time_hobbies"] = false;
    updateFields["hobbies"] = true;
    updateFields["time_hobbies"] = false;

    if (hobbiesSelect.value == "Ninguno") {
      document
        .getElementById(`group__time_hobbies`)
        .classList.remove("form__group-incorrect");
      document
        .getElementById(`group__time_hobbies`)
        .classList.add("form__group-correct");
      document
        .querySelector(`#group__time_hobbies .form__input-error`)
        .classList.remove("form__input-error-active");
      timeSelect.disabled = true;
      fields["time_hobbies"] = true;
      updateFields["time_hobbies"] = true;
    }
  } else {
    document
      .getElementById(`group__hobbies`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__hobbies`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__hobbies .form__input-error`)
      .classList.add("form__input-error-active");

    fields["hobbies"] = false;
    updateFields["hobbies"] = false;

    timeSelect.getElementsByTagName("option")[0].selected = true;
    timeSelect.disabled = true;
  }
});

//  Procedimiento que coloca en el campo edad, la edad que calcula la función calculateAge()
document.getElementById("dateNac").addEventListener("change", function () {
  if (this.value) {
    document.getElementById("edad").value = calculateAge(this.value);
  }
});

//  Función que calcula la edad del sujeto a partir de su fecha de nacimiento
const calculateAge = (dateBirth) => {
  const dateNow = new Date();
  const yearNow = parseInt(dateNow.getFullYear());
  const monthNow = parseInt(dateNow.getMonth()) + 1;
  const dayNow = parseInt(dateNow.getDate());

  const yearBirth = parseInt(String(dateBirth).substring(0, 4));
  const monthBirth = parseInt(String(dateBirth).substring(5, 7));
  const dayBirth = parseInt(String(dateBirth).substring(8, 10));

  let age = yearNow - yearBirth;

  if (monthNow < monthBirth) {
    age--;
  } else if (monthNow === monthBirth) {
    if (dayNow < dayBirth) {
      age--;
    }
  }

  return age;
};

//  Función que valida si el objeto fields es true = los campos se han llenado
function validateFields(obj) {
  for (let key in obj) {
    if (obj.hasOwnProperty(key) && !obj[key]) {
      return false;
    }
  }
  return true;
}

//  Procedimiento que confirma que el formulario fue contestado correctamente
if(proceedingForm){
  proceedingForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    if (validateFields(fields)) {
      document.getElementById("form-proceeding").submit(); // Envía el formulario si el usuario confirma
    }
  });
}


//  Función que aplica mayúsculas al inicio de cada palabra en una oración dada
function capitalizeFirstLetter(str) {
  var words = str.split(" ");
  for (var i = 0; i < words.length; i++) {
    words[i] = words[i].charAt(0).toUpperCase() + words[i].substring(1);
  }
  return words.join(" ");
}

//  Función que aplica mayúsculas al inicio de una oración dada
function capitalizeFirstWord(text) {
  const words = text.split(" ");
  words[0] = words[0].charAt(0).toUpperCase() + words[0].slice(1);
  return words.join(" ");
}


//  Procedimiento que confirma que el formulario fue contestado correctamente
if(updateForm){
  updateForm.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    if (validateFields(updateFields)) {
      document.getElementById("update-proceeding").submit(); // Envía el formulario si el usuario confirma
    }
  });                                                                        
}
