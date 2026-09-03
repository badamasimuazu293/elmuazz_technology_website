document.addEventListener("DOMContentLoaded", function () {

    const menuButton = document.getElementById(
        "mobileMenuButton"
    );

    const mobileNavigation = document.getElementById(
        "mobileNavigation"
    );

    const siteHeader = document.querySelector(
        ".site-header"
    );


    /* =========================================
       MOBILE MENU
    ========================================= */

    if (menuButton && mobileNavigation) {

        menuButton.addEventListener("click", function () {

            const isOpen =
                mobileNavigation.classList.toggle("open");

            menuButton.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );

            menuButton.setAttribute(
                "aria-label",
                isOpen
                    ? "Close navigation menu"
                    : "Open navigation menu"
            );

        });


        /* Close menu after clicking a link */

        const mobileLinks =
            mobileNavigation.querySelectorAll("a");

        mobileLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                mobileNavigation.classList.remove("open");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

                menuButton.setAttribute(
                    "aria-label",
                    "Open navigation menu"
                );

            });

        });

    }


    /* =========================================
       HEADER SCROLL
    ========================================= */

    if (siteHeader) {

        function updateHeader() {

            if (window.scrollY > 20) {
                siteHeader.classList.add("scrolled");
            } else {
                siteHeader.classList.remove("scrolled");
            }

        }

        window.addEventListener(
            "scroll",
            updateHeader,
            { passive: true }
        );

        updateHeader();

    }

});