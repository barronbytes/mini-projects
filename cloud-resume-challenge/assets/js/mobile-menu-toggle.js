const mobileMenu = document.querySelector("#mobile-section");
const buttons = document.querySelectorAll(".toggle-open, .toggle-close");

buttons.forEach((button) => {
  button.addEventListener("click", toggleMenu);
  button.addEventListener("keydown", toggleMenu);
});

function toggleMenu(event) {
  // Handle clicks, Enter, or Space key
  if (event.type === "click" || event.key === "Enter" || event.key === " ") {
    if (event.key === " ") event.preventDefault();

    // Use currentTarget to reliably reference the button
    const isOpening = event.currentTarget.classList.contains("toggle-open");
    mobileMenu.setAttribute("data-visible", isOpening ? "true" : "false");
    mobileMenu.setAttribute("aria-expanded", isOpening ? "true" : "false");
  }
}