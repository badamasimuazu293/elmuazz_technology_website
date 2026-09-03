document.addEventListener("DOMContentLoaded", function () {

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

        menuButton.addEventListener("click", function () {

            const isOpen =
                mobileNavigation.classList.toggle("open");

            menuButton.setAttribute(
                "aria-expanded",
                isOpen ? "true" : "false"
            );

        });


        const mobileLinks =
            mobileNavigation.querySelectorAll(
                "a:not(.mobile-whatsapp)"
            );


        mobileLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                mobileNavigation.classList.remove("open");

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

        window.addEventListener("scroll", function () {

            if (window.scrollY > 20) {

                siteHeader.classList.add("scrolled");

            } else {

                siteHeader.classList.remove("scrolled");

            }

        });

    }

});