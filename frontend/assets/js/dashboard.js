document.addEventListener("DOMContentLoaded", async function() {
    const navButtons = document.querySelectorAll(".nav-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    navButtons.forEach(button => {
        button.addEventListener("click", function() {
            const sectionId = this.getAttribute("data-section");

            tabContents.forEach(content => {
                content.classList.remove("active");
            });

            document.getElementById(sectionId).classList.add("active");
        });
    });

    // Logout functionality
    document.getElementById("logout-btn").addEventListener("click", function() {
        localStorage.removeItem("token");
        window.location.href = "../frontend/index.html";
    });

    // Fetch and display username
    const usernameDisplay = document.getElementById("username");
    const token = localStorage.getItem("token");

    if (!token) {
        alert("Timed out")
        window.location.href = "../frontend/index.html";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/api/dashboard", {
            headers: {
                Authorization: `Bearer ${token}`
            }
        });

        const data = await response.json();
        if (response.ok) {
            usernameDisplay.textContent = data.username;
        } else {
            usernameDisplay.textContent = "User not found";
        }
    } catch (error) {
        console.error("Failed to fetch user:", error);
        alert("Error loading user info");
    }
});