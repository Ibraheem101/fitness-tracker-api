document.addEventListener("DOMContentLoaded", async () =>{
    const token = localStorage.getItem("token");
    if (!token) {
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
            document.getElementById("username-display").textContent = `Hi, Welcome ${data.username}`;
        } else {
            alert("User not found");
        }
    } catch (error) {
        console.error("Failed to fetch user:", error);
        alert("Error loading user info");
    }

});