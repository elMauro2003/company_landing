const passwordInput1 = document.querySelector("#floatingInputPassword1");
const eyeSlashIcon1 = document.querySelector("#eyeSlashIcon1");
const eyeIcon1 = document.querySelector("#eyeIcon1");
const passwordInput2 = document.querySelector("#floatingInputPassword2");
const eyeSlashIcon2 = document.querySelector("#eyeSlashIcon2");
const eyeIcon2 = document.querySelector("#eyeIcon2");


document.addEventListener("DOMContentLoaded", function () {

  eyeSlashIcon1.addEventListener("click", function () {
    if (passwordInput1.type === "password") {
      passwordInput1.type = "text";
      eyeSlashIcon1.classList.add("d-none");
      eyeIcon1.classList.remove("d-none");
    }
  });
  eyeIcon1.addEventListener("click", function () {
    if (passwordInput1.type === "text") {
      passwordInput1.type = "password";
      eyeSlashIcon1.classList.remove("d-none");
      eyeIcon1.classList.add("d-none");
    }
  });
  eyeSlashIcon2.addEventListener("click", function () {
    if (passwordInput2.type === "password") {
      passwordInput2.type = "text";
      eyeSlashIcon2.classList.add("d-none");
      eyeIcon2.classList.remove("d-none");
    }
  });
  eyeIcon2.addEventListener("click", function () {
    if (passwordInput2.type === "text") {
      passwordInput2.type = "password";
      eyeSlashIcon2.classList.remove("d-none");
      eyeIcon2.classList.add("d-none");
    }
  });
});

