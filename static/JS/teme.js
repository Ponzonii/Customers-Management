// Function to change the theme
function changeTeme() {
  const body = document.body;
  const html = document.documentElement;
  const icone = document.getElementById("icon-teme");

  // Adds a slight delay before switching the theme
  setTimeout(() => {
    // Check the current theme and switch accordingly
    if (html.getAttribute("data-bs-theme") === "light") {
      html.setAttribute("data-bs-theme", "dark"); // Set dark theme
      body.id = "body-dark";
      localStorage.setItem("tema", "dark"); // Save the theme preference

      // Change the theme icon
      icone.classList.replace(
        "mdi-moon-waning-crescent",
        "mdi-white-balance-sunny"
      );
    } else {
      html.setAttribute("data-bs-theme", "light"); // Set light theme
      body.id = "body-light";
      localStorage.setItem("tema", "light"); // Save the theme preference

      // Change the theme icon back
      icone.classList.replace(
        "mdi-white-balance-sunny",
        "mdi-moon-waning-crescent"
      );
    }
  }, 300); // 300ms delay for smooth transition
}

// Apply the saved theme when the page loads
document.addEventListener("DOMContentLoaded", () => {
  const temaSalvo = localStorage.getItem("tema") || "light"; // Get saved theme or default to light
  const icone = document.getElementById("icon-teme");

  document.documentElement.setAttribute("data-bs-theme", temaSalvo); // Apply the saved theme
  document.body.id = temaSalvo === "dark" ? "body-dark" : "body-light";

  // Set the correct icon on page load
  if (temaSalvo === "dark") {
    icone.classList.replace(
      "mdi-moon-waning-crescent",
      "mdi-white-balance-sunny"
    );
  } else {
    icone.classList.replace(
      "mdi-white-balance-sunny",
      "mdi-moon-waning-crescent"
    );
  }
});
