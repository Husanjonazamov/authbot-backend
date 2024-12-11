// Dynamic Username
document.addEventListener("DOMContentLoaded", function () {
    const username = "🙈"; // Bu yerni backenddan keladigan foydalanuvchi ismi bilan almashtiring
    document.getElementById("username").textContent = username;

    // Logout functionality
    document.getElementById("logout").addEventListener("click", function () {
        alert("You have been logged out.");
        // Log out qilish kodini bu yerga yozing.
    });
});
