document.addEventListener("DOMContentLoaded", function () {

    /* =========================================
       ELEMENTS
    ========================================= */

    const menuButton =
        document.getElementById("mobileMenuButton");

    const mobileNavigation =
        document.getElementById("mobileNavigation");

    const siteHeader =
        document.querySelector(".site-header");


    /* =========================================
       MOBILE MENU
    ========================================= */

    if (menuButton && mobileNavigation) {

        menuButton.addEventListener("click", function (event) {

            event.preventDefault();
            event.stopPropagation();

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


        /* =========================================
           MOBILE NAVIGATION LINKS
        ========================================= */

        const mobileLinks =
            mobileNavigation.querySelectorAll("a");


        mobileLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                /*
                 * Do not prevent the default action.
                 * Django navigation links must be
                 * allowed to navigate normally.
                 */

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
       CLOSE MOBILE MENU WHEN CLICKING OUTSIDE
    ========================================= */

    document.addEventListener("click", function (event) {

        if (!menuButton || !mobileNavigation) {
            return;
        }

        const clickedInsideMenu =
            mobileNavigation.contains(event.target);

        const clickedButton =
            menuButton.contains(event.target);

        if (
            !clickedInsideMenu &&
            !clickedButton &&
            mobileNavigation.classList.contains("open")
        ) {

            mobileNavigation.classList.remove("open");

            menuButton.setAttribute(
                "aria-expanded",
                "false"
            );

            menuButton.setAttribute(
                "aria-label",
                "Open navigation menu"
            );

        }

    });


    /* =========================================
       CLOSE MENU WHEN WINDOW RESIZES
    ========================================= */

    window.addEventListener("resize", function () {

        if (
            window.innerWidth > 850 &&
            mobileNavigation
        ) {

            mobileNavigation.classList.remove("open");

            if (menuButton) {

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

                menuButton.setAttribute(
                    "aria-label",
                    "Open navigation menu"
                );

            }

        }

    });


    /* =========================================
       HEADER SCROLL EFFECT
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


        /* Run once when page loads */

        updateHeader();

    }

});