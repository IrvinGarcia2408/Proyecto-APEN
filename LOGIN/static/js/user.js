// Función para capitalizar las iniciales de cada palabra
function capitalizeFirstLetter(string) {
  return string
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join(" ");
}

// Validate all fields on page load for edit form only
document.addEventListener("DOMContentLoaded", () => {
  const editForm = document.getElementById("editForm");
  if (editForm) {
    const fieldsToValidate = [
      "name",
      "first_last_name",
      "second_last_name",
      "username",
      "email",
    ];
    fieldsToValidate.forEach((field) => {
      const inputElement = document.getElementById(field);
      if (inputElement) {
        validateForm({ target: inputElement });
      }
    });
  } else {
    // Initialize validation icons for both forms
    const allFields = [
      "name",
      "first_last_name",
      "second_last_name",
      "username",
      "email",
      "password1",
      "password2",
    ];

    allFields.forEach((field) => {
      const inputElement = document.getElementById(field);
      if (inputElement) {
        const validationStateElement = inputElement.nextElementSibling;
        if (
          validationStateElement &&
          validationStateElement.classList.contains("form__validation-state")
        ) {
          validationStateElement.classList.add("fa-times-circle");
        }
      }
    });
  }
});

const forms = {
  register: document.getElementById("registerForm"),
  edit: document.getElementById("editForm"),
};

const inputs = document.querySelectorAll(
  "#registerForm input, #editForm input"
);

const expressions = {
  user: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, números, guión y guión bajo
  personName: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos
  lastName: /^[a-zA-ZÀ-ÿ]{1,30}$/, // Letras, pueden llevar acentos
  email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
  password: /^.{8,12}$/, // 8 a 12 dígitos
};

const fields = {
  name: false,
  flastName: false,
  slastName: false,
  username: false,
  email: false,
  password: false,
};

const validateForm = (e) => {
  switch (e.target.name) {
    case "name":
      validateField(expressions.personName, e.target, "name");
      document.getElementById("name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "first_last_name":
      validateField(expressions.lastName, e.target, "flastName");
      document.getElementById("first_last_name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "second_last_name":
      validateField(expressions.lastName, e.target, "slastName");
      document.getElementById("second_last_name").value = capitalizeFirstLetter(
        e.target.value
      );
      break;
    case "username":
      validateField(expressions.user, e.target, "username");
      break;
    case "email":
      validateField(expressions.email, e.target, "email");
      break;
    case "password1":
      if (e.target.value) {
        validateField(expressions.password, e.target, "password1");
        validatePassword();
      }
      break;
    case "password2":
      if (document.getElementById("password1").value) {
        validatePassword();
      }
      break;
  }
};

const validateField = (expression, input, field) => {
  if (expression.test(input.value)) {
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-correct");
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-incorrect");
    document
      .querySelector(`#group__${field} .form__validation-state`)
      .classList.add("fa-check-circle");
    document
      .querySelector(`#group__${field} .form__validation-state`)
      .classList.remove("fa-times-circle");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.remove("form__input-error-active");
    fields[field] = true;
  } else {
    document
      .getElementById(`group__${field}`)
      .classList.add("form__group-incorrect");
    document
      .getElementById(`group__${field}`)
      .classList.remove("form__group-correct");
    document
      .querySelector(`#group__${field} .form__validation-state`)
      .classList.add("fa-times-circle");
    document
      .querySelector(`#group__${field} .form__validation-state`)
      .classList.remove("fa-check-circle");
    document
      .querySelector(`#group__${field} .form__input-error`)
      .classList.add("form__input-error-active");
    fields[field] = false;
  }
};

const validatePassword = () => {
  const inputPassword1 = document.getElementById("password1");
  const inputPassword2 = document.getElementById("password2");

  if (inputPassword1.value === inputPassword2.value) {
    document
      .getElementById("group__password2")
      .classList.remove("form__group-incorrect");
    document
      .getElementById("group__password2")
      .classList.add("form__group-correct");
    document
      .querySelector("#group__password2 .form__validation-state")
      .classList.add("fa-check-circle");
    document
      .querySelector("#group__password2 .form__validation-state")
      .classList.remove("fa-times-circle");
    document
      .querySelector("#group__password2 .form__input-error")
      .classList.remove("form__input-error-active");
    fields.password = true;
  } else {
    document
      .getElementById("group__password2")
      .classList.add("form__group-incorrect");
    document
      .getElementById("group__password2")
      .classList.remove("form__group-correct");
    document
      .querySelector("#group__password2 .form__validation-state")
      .classList.add("fa-times-circle");
    document
      .querySelector("#group__password2 .form__validation-state")
      .classList.remove("fa-check-circle");
    document
      .querySelector("#group__password2 .form__input-error")
      .classList.add("form__input-error-active");
    fields.password = false;
  }
};

inputs.forEach((input) => {
  input.addEventListener("keyup", validateForm);
  input.addEventListener("blur", validateForm);
});

const submitForm = (e, formType) => {
  const passwordOptional =
    formType === "edit" &&
    !document.getElementById("password1").value &&
    !document.getElementById("password2").value;

  if (
    fields.name &&
    fields.flastName &&
    fields.slastName &&
    fields.username &&
    fields.email &&
    (fields.password || passwordOptional)
  ) {
    // Envía el formulario
  } else {
    e.preventDefault();
    document
      .getElementById("form__message")
      .classList.add("form__message-active");
  }
};

if (forms.register) {
  forms.register.addEventListener("submit", (e) => submitForm(e, "register"));
}

if (forms.edit) {
  forms.edit.addEventListener("submit", (e) => submitForm(e, "edit"));
}
