document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault(); // prevent default form submit

    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const verify_password = document.getElementById("verify_password").value;

    if (password !== verify_password) {
        alert("Passwords do not match");
        return;
    }
    try {
        const response = await fetch("http://127.0.0.1:5000/api/create-user", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, email, password })
        });

        const data = await response.json();

        if (response.ok) {
            // redirect to login
            alert("Registration successful!");
            window.location.href = "../frontend/index.html";
        } else {
            alert(data.error || "Registration failed");
        }
    } catch (error) {
        console.error("Error during registration:", error);
        alert("Something went wrong. Please try again.");
    }


});
