document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("mobileMenuButton");
    const mobileNavigation = document.getElementById("mobileNavigation");
    const siteHeader = document.querySelector(".site-header");

    /* =========================================
       MOBILE MENU
    ========================================= */
    if (menuButton && mobileNavigation) {
        
        function closeMobileMenu() {
            mobileNavigation.classList.remove("open");
            menuButton.classList.remove("active");
            menuButton.setAttribute("aria-expanded", "false");
            menuButton.setAttribute("aria-label", "Open navigation menu");
        }

        function toggleMobileMenu() {
            const isOpen = mobileNavigation.classList.toggle("open");
            menuButton.classList.toggle("active", isOpen);
            
            menuButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
            menuButton.setAttribute("aria-label", isOpen ? "Close navigation menu" : "Open navigation menu");
        }

        // Toggle menu on button click
        menuButton.addEventListener("click", toggleMobileMenu);

        // Close menu when clicking navigation links
        const mobileLinks = mobileNavigation.querySelectorAll("a");
        mobileLinks.forEach(function (link) {
            link.addEventListener("click", closeMobileMenu);
        });

        // Close menu when clicking outside header area
        document.addEventListener("click", function (event) {
            if (!siteHeader.contains(event.target) && mobileNavigation.classList.contains("open")) {
                closeMobileMenu();
            }
        });

        // Close menu on ESC key press
        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && mobileNavigation.classList.contains("open")) {
                closeMobileMenu();
            }
        });
    }

    /* =========================================
       HEADER SCROLL
    ========================================= */
    if (siteHeader) {
        function updateHeader() {
            siteHeader.classList.toggle("scrolled", window.scrollY > 20);
        }

        window.addEventListener("scroll", updateHeader, { passive: true });
        updateHeader();
    }
});