document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", (e) => {
            const username = form.username.value.trim();
            const password = form.password.value.trim();
            if (!username || !password) {
                e.preventDefault();
                alert("Por favor, preencha todos os campos!");
            }
        });
    }

    const messages = document.querySelectorAll("li");
    messages.forEach(msg => {
        setTimeout(() => {
            msg.style.display = "none";
        }, 3000);
    });

    const togglePassword = document.querySelector("#togglePassword");
    const passwordField = document.querySelector("input[name='password']");
    if (togglePassword && passwordField) {
        togglePassword.addEventListener("click", () => {
            const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
            passwordField.setAttribute("type", type);
            togglePassword.textContent = type === "password" ? "Mostrar" : "Ocultar";
        });
    }
});
