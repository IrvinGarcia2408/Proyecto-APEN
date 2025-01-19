document.addEventListener("DOMContentLoaded", function () {
  searchState(document.getElementById("country"));
  document.getElementById("state").value = document.getElementById("stateDB").value;
 

  initCheck(
    document.getElementById("talk_other_language"),
    document.getElementById("talk_other_languageDB").value,
    "other_languages",
    document.getElementById("other_languagesDB").value
  );
  document.getElementById("edad").value = calculateAge(document.getElementById("dateNac").value);
  document.getElementById("gender").value =
    document.getElementById("genderDB").value;
  document.getElementById("laterality").value =
    document.getElementById("lateralityDB").value;
  document.getElementById("instrument").value =
    document.getElementById("instrumentDB").value;
  if (document.getElementById("instrument").value != "Ninguno") {
    document.getElementById("time_instrument").disabled = false;
    document.getElementById("time_instrument").value =
      document.getElementById("time_instrumentDB").value;
  }
  document.getElementById("hobbies").value =
    document.getElementById("hobbiesDB").value;
  if (document.getElementById("hobbies").value != "Ninguno") {
    document.getElementById("time_hobbies").disabled = false;
    document.getElementById("time_hobbies").value =
      document.getElementById("time_hobbiesDB").value;
  }
  document.getElementById("civil_status").value =
    document.getElementById("civil_statusDB").value;
  document.getElementById("religion").value =
    document.getElementById("religionDB").value;

  initCheck(
    document.getElementById("hyperthension"),
    document.getElementById("hyperthensionDB").value,
    "time_hyperthension",
    document.getElementById("time_hyperthensionDB").value
  );
  initCheck(
    document.getElementById("pulmonary_diseases"),
    document.getElementById("pulmonary_diseasesDB").value,
    "time_pulmonary_diseases",
    document.getElementById("time_pulmonary_diseasesDB").value
  );
  initCheck(
    document.getElementById("alcoholism"),
    document.getElementById("alcoholismDB").value,
    "time_alcoholism",
    document.getElementById("time_alcoholismDB").value
  );
  initCheck(
    document.getElementById("drugs"),
    document.getElementById("drugsDB").value,
    "time_drugs",
    document.getElementById("time_drugsDB").value
  );
  initCheck(
    document.getElementById("decrease_senses"),
    document.getElementById("decrease_sensesDB").value,
    "time_decrease_senses",
    document.getElementById("time_decrease_sensesDB").value
  );
  initCheck(
    document.getElementById("craniocerebral_trauma"),
    document.getElementById("craniocerebral_traumaDB").value,
    "time_craniocerebral_trauma",
    document.getElementById("time_craniocerebral_traumaDB").value
  );
  initCheck(
    document.getElementById("diabetes"),
    document.getElementById("diabetesDB").value,
    "time_diabetes",
    document.getElementById("time_diabetesDB").value
  );
  initCheck(
    document.getElementById("hypothyroidism"),
    document.getElementById("hypothyroidismDB").value,
    "time_hypothyroidism",
    document.getElementById("time_hypothyroidismDB").value
  );
  initCheck(
    document.getElementById("strokes"),
    document.getElementById("strokesDB").value,
    "time_strokes",
    document.getElementById("time_strokesDB").value
  );
  initCheck(
    document.getElementById("others_diseases"),
    document.getElementById("others_diseasesDB").value,
    "details_others_diseases",
    document.getElementById("details_others_diseasesDB").value
  );

  if (document.getElementById('medical_history').value.trim() === 'None' || document.getElementById('medical_history').value.trim() === '') {
    document.getElementById('medical_history').value = ''; // Limpiar el contenido
  }
  document.getElementById('medical_history').value.trim();

});

function initCheck(check, db, combo, comboDB) {
  console.log(db);
  if (db === "True") {
    check.checked = true;
    document.getElementById(combo).value = comboDB;
    document.getElementById(combo).disabled = false;
  } else {
    check.checked = false;
    document.getElementById(combo).value = "";
    document.getElementById(combo).disabled = true;
  }
}

function searchState(country){
  country.required  = true;
  var xhr = new XMLHttpRequest();
  if (
    country.value != "" &&
    country.options[country.value].textContent != "Otro"
  ) {
    document.getElementById("state").required = true;
    document.getElementById("municipality").required = true;
    xhr.open("GET", "/expedientes/crear/estados/?country=" + country.value, true);
    xhr.onload = function () {
      if (this.status === 200) {
        var states = JSON.parse(this.responseText);
        console.log(states)
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
        document.getElementById("state").value = document.getElementById("stateDB").value;
        // actualizar municipios
        if (document.getElementById("state").value != "") {
          searchMunicipality(document.getElementById("state"))
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
}

function searchMunicipality(state){
  var stateId = state.value;
  state.required  = true;

  var xhr = new XMLHttpRequest();
  if (stateId != "") {
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
        document.getElementById("municipality").disabled = false;


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
        document.getElementById("municipality").value = document.getElementById("municipalityDB").value;
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
}

