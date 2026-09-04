document.addEventListener("DOMContentLoaded", function () {

    const menuButton = document.getElementById("mobileMenuButton");
    const mobileNavigation = document.getElementById("mobileNavigation");
    const siteHeader = document.querySelector(".site-header");


    /* =========================================
       MOBILE MENU
    ========================================= */

    if (menuButton && mobileNavigation) {

        menuButton.addEventListener("click", function (event) {

            event.preventDefault();
            event.stopPropagation();

            const isOpen =
                mobileNavigation.classList.toggle("open");

            menuButton.classList.toggle("active", isOpen);

            menuButton.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );

            console.log(
                "Mobile menu:",
                isOpen ? "OPEN" : "CLOSED"
            );

        });


        /* Close menu when clicking a navigation link */

        const mobileLinks =
            mobileNavigation.querySelectorAll("a");


        mobileLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                mobileNavigation.classList.remove("open");

                menuButton.classList.remove("active");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            });

        });

    }


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
            updateHeader
        );

        updateHeader();

    }

});