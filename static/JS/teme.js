function mudarTema() {
  const body = document.body;
  const html = document.documentElement;
  const icone = document.getElementById("tema-icone");

  setTimeout(() => {
    if (html.getAttribute("data-bs-theme") === "light") {
      html.setAttribute("data-bs-theme", "dark");
      body.id = "body-dark";
      localStorage.setItem("tema", "dark");
      icone.classList.replace(
        "mdi-moon-waning-crescent",
        "mdi-white-balance-sunny"
      );
    } else {
      html.setAttribute("data-bs-theme", "light");
      body.id = "body-light";
      localStorage.setItem("tema", "light");
      icone.classList.replace(
        "mdi-white-balance-sunny",
        "mdi-moon-waning-crescent"
      );
    }
  }, 300);
}

// Aplicar o tema salvo ao carregar a página
document.addEventListener("DOMContentLoaded", () => {
  const temaSalvo = localStorage.getItem("tema") || "light";
  const icone = document.getElementById("tema-icone");

  document.documentElement.setAttribute("data-bs-theme", temaSalvo);
  document.body.id = temaSalvo === "dark" ? "body-dark" : "body-light";

  // Define o ícone correto ao carregar a página
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
