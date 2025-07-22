document.addEventListener("DOMContentLoaded", () => {
    const PORTFOLIO_ITEMS = document.querySelectorAll(".portfolio-2 .group");
    const PORTFOLIO_LIST = document.querySelector(".portfolio-2"); // Select the unordered list

    // Function to adjust items based on screen size
    function adjustPortfolioItems() {
        const isSmallScreen = window.innerWidth <= 540; // Check screen size
        if (isSmallScreen) {
            // Keep only the first two items if the screen size is 540px or less
            PORTFOLIO_ITEMS.forEach((item, index) => {
                item.style.display = index < 2 ? "block" : "none"; // Hide items beyond the second
            });
        } else {
            // Restore all items for larger screens
            PORTFOLIO_ITEMS.forEach((item) => {
                item.style.display = "block"; // Show all items
            });
        }
    }

    // Call adjustPortfolioItems on load and on resize
    adjustPortfolioItems(); // Adjust items on initial load
    window.addEventListener("resize", adjustPortfolioItems); // Adjust items on window resize

    // Event listeners for dynamic content toggle
    PORTFOLIO_ITEMS.forEach((item) => {
        const PORTFOLIO_IMAGE = item.querySelector("a"); // Target the original content
        const PORTFOLIO_INFO = item.querySelector(".project-item-default"); // Target the PORTFOLIO_INFO element

        // Define new content
        const DYNAMIC_CONTENT = `
            <p class="section-subtitle">Adipiscing, elit sapien hendrerit vulputate vehicula.</p>
            <a class="button footer-cta" href="#" title="Check Out The Details">Open My Project</a>
        `;

        // Add event listeners for hover, focus, and touch interactions
        item.addEventListener("mouseenter", () => toggleContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO, DYNAMIC_CONTENT));
        item.addEventListener("mouseleave", () => revertContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO));
        item.addEventListener("focus", () => toggleContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO, DYNAMIC_CONTENT));
        item.addEventListener("blur", () => revertContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO));
    });

    function toggleContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO, DYNAMIC_CONTENT) {
        if (item.getAttribute("aria-expanded") === "true") return;

        // Hide the original image
        PORTFOLIO_IMAGE.style.display = "none";

        // Update PORTFOLIO_INFO content and switch class
        PORTFOLIO_INFO.innerHTML = DYNAMIC_CONTENT;
        PORTFOLIO_INFO.classList.remove("project-item-default");
        PORTFOLIO_INFO.classList.add("project-item");
        PORTFOLIO_INFO.setAttribute("aria-hidden", "false");

        // Update item attributes
        item.setAttribute("aria-expanded", "true");
    }

    function revertContent(item, PORTFOLIO_IMAGE, PORTFOLIO_INFO) {
        if (item.getAttribute("aria-expanded") === "false") return;

        // Show the original image
        PORTFOLIO_IMAGE.style.display = "";

        // Clear PORTFOLIO_INFO content and reset class
        PORTFOLIO_INFO.innerHTML = "";
        PORTFOLIO_INFO.classList.remove("project-item");
        PORTFOLIO_INFO.classList.add("project-item-default");
        PORTFOLIO_INFO.setAttribute("aria-hidden", "true");

        // Reset the attributes
        item.setAttribute("aria-expanded", "false");
    }
});
