document.addEventListener("DOMContentLoaded", function () {

    /* =========================================
       ELEMENTS
    ========================================= */

    const menuButton = document.getElementById("mobileMenuButton");
    const mobileNavigation = document.getElementById("mobileNavigation");
    const siteHeader = document.querySelector(".site-header");


    /* =========================================
       HELPER FUNCTIONS
    ========================================= */

    function setMenuState(isOpen) {
        if (!mobileNavigation || !menuButton) return;

        // Toggle visibility classes on both menu and button (for CSS animation)
        mobileNavigation.classList.toggle("active", isOpen);
        menuButton.classList.toggle("active", isOpen);

        // Update ARIA attributes
        menuButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
        menuButton.setAttribute(
            "aria-label",
            isOpen ? "Close navigation menu" : "Open navigation menu"
        );
    }

    function closeMenu() {
        setMenuState(false);
    }


    /* =========================================
       MOBILE MENU TOGGLE
    ========================================= */

    if (menuButton && mobileNavigation) {

        menuButton.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();

            const isCurrentlyOpen = mobileNavigation.classList.contains("active");
            setMenuState(!isCurrentlyOpen);
        });


        /* Close on link click */
        const mobileLinks = mobileNavigation.querySelectorAll("a");
        mobileLinks.forEach(function (link) {
            link.addEventListener("click", closeMenu);
        });

    }


    /* =========================================
       GLOBAL DISMISSALS (CLICK OUTSIDE & ESCAPE)
    ========================================= */

    document.addEventListener("click", function (event) {
        if (!menuButton || !mobileNavigation) return;

        const clickedInsideMenu = mobileNavigation.contains(event.target);
        const clickedButton = menuButton.contains(event.target);

        if (!clickedInsideMenu && !clickedButton) {
            closeMenu();
        }
    });

    // Close menu when pressing Escape key
    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeMenu();
        }
    });


    /* =========================================
       RESIZE LISTENER
    ========================================= */

    window.addEventListener("resize", function () {
        if (window.innerWidth > 850) {
            closeMenu();
        }
    });


    /* =========================================
       HEADER SCROLL EFFECT
    ========================================= */

    if (siteHeader) {
        function updateHeader() {
            siteHeader.classList.toggle("scrolled", window.scrollY > 20);
        }

        window.addEventListener("scroll", updateHeader, { passive: true });
        updateHeader();
    }

});