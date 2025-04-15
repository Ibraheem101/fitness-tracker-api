document.getElementById("login-form").addEventListener("submit", async function (e) {
    e.preventDefault(); // prevent default form submit

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            // save token, maybe redirect
            localStorage.setItem("token", data.token);
            alert("Login successful!");
            // window.location.href = "/dashboard.html"; // to do later
        } else {
            alert(data.error || "Login failed");
        }
    } catch (error) {
        console.error("Error during login:", error);
        alert("Something went wrong. Please try again.");
    }
});
