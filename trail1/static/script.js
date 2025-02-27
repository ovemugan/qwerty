document.addEventListener("DOMContentLoaded", function () {
    // Registration Logic
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            let name = document.getElementById("name").value;
            let password = document.getElementById("password").value;
            let confirmPassword = document.getElementById("confirmPassword").value;

            if (password !== confirmPassword) {
                alert("Passwords do not match!");
                return;
            }

            let userData = { name: name, password: password };
            localStorage.setItem(name, JSON.stringify(userData));
            alert("Registration Successful! Redirecting to login...");
            window.location.href = "login.html";
        });
    }

    // Login Logic
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            let name = document.getElementById("loginName").value;
            let password = document.getElementById("loginPassword").value;
            let storedUser = localStorage.getItem(name);

            if (!storedUser) {
                alert("User not found!");
                return;
            }

            let userData = JSON.parse(storedUser);
            if (userData.password === password) {
                alert("Login Successful!");
                sessionStorage.setItem("loggedInUser", name);
                window.location.href = "index.html";
            } else {
                alert("Incorrect password!");
            }
        });
    }
});

// Logout Function
function logout() {
    fetch('/logout').then(() => {
        window.location.href = "exit.html";
    });
}
