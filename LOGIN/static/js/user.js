const registerForm = document.getElementById("registerForm");
const inputs = document.querySelectorAll("#registerForm input");

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
  password: false
}

const validateForm = (e) => {
  switch (e.target.name) {
    case "name":
      validateField(expressions.personName, e.target,'name');
      document.getElementById("name").value = capitalizeFirstLetter(e.target.value);
      break;
    case "first_last_name":
      validateField(expressions.lastName, e.target,'flastName');
      document.getElementById("first_last_name").value = capitalizeFirstLetter(e.target.value);
      break;
    case "second_last_name":
      validateField(expressions.lastName, e.target,'slastName');
      document.getElementById("second_last_name").value = capitalizeFirstLetter(e.target.value);
      break;
    case "username":
        validateField(expressions.user, e.target,'username');
      break;
      case "email":
        validateField(expressions.email, e.target,'email');
      break;
    case "password1":
      validateField(expressions.password, e.target,'password1');
      validatePassword();
      break;
    case "password2":
      validatePassword();
      break;
  }
};

const validateField = (expression, input, field) => {
  if(expression.test(input.value)){
    document.getElementById(`group__${field}`).classList.remove("form__group-incorrect");
    document.getElementById(`group__${field}`).classList.add("form__group-correct");
    document.querySelector(`#group__${field} .form__validation-state`).classList.add("fa-check-circle");
    document.querySelector(`#group__${field} .form__validation-state`).classList.remove("fa-times-circle");
    document.querySelector(`#group__${field} .form__input-error`).classList.remove("form__input-error-active");
    fields[field] = true;
  }else{
      document.getElementById(`group__${field}`).classList.add("form__group-incorrect");
      document.getElementById(`group__${field}`).classList.remove("form__group-correct");
      document.querySelector(`#group__${field} .form__validation-state`).classList.add("fa-times-circle");
      document.querySelector(`#group__${field} .form__validation-state`).classList.remove("fa-check-circle");
      document.querySelector(`#group__${field} .form__input-error`).classList.add("form__input-error-active");
      fields[field] = false;
  }
}

const validatePassword = () => {
  const inputPassword1 = document.getElementById("password1");
  const inputPassword2 = document.getElementById("password2");

  if(inputPassword1.value != inputPassword2.value){
    document.getElementById(`group__password2`).classList.add("form__group-incorrect");
    document.getElementById(`group__password2`).classList.remove("form__group-correct");
    document.querySelector(`#group__password2 .form__validation-state`).classList.add("fa-times-circle");
    document.querySelector(`#group__password2 .form__validation-state`).classList.remove("fa-check-circle");
    document.querySelector(`#group__password2 .form__input-error`).classList.add("form__input-error-active");
    fields["password"] = false;
  }else{
    document.getElementById(`group__password2`).classList.remove("form__group-incorrect");
    document.getElementById(`group__password2`).classList.add("form__group-correct");
    document.querySelector(`#group__password2 .form__validation-state`).classList.remove("fa-times-circle");
    document.querySelector(`#group__password2 .form__validation-state`).classList.add("fa-check-circle");
    document.querySelector(`#group__password2 .form__input-error`).classList.remove("form__input-error-active");
    fields["password"] = true;
  }

}

inputs.forEach((input) => {
  input.addEventListener("keyup", validateForm);
  input.addEventListener("blur", validateForm);
});

registerForm.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log(fields.name);
  console.log(fields.flastName);
  console.log(fields.slastName);
  console.log(fields.username);
  console.log(fields.email);
  console.log(fields.password);
  if(fields.name && fields.flastName && fields.slastName && fields.username && fields.email && fields.password){
    // aqui muestro el modal
    document.getElementById('registerForm').submit(); // Envía el formulario si el usuario confirma
  }else{
    document.getElementById("form__message").classList.add("form__message-active");
    setTimeout(() => {
      document.getElementById("form__message").classList.remove("form__message-active");
    }, 5000)
  }
});

function capitalizeFirstLetter(str){
  var words = str.split(' ');
  for (var i = 0; i < words.length; i++){
    words[i] = words[i].charAt(0).toUpperCase() + words[i].substring(1);
  }
  return words.join(' ');
}