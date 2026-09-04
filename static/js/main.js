
document.addEventListener("DOMContentLoaded", function () {

    console.log("Elmuazz main.js loaded");

    const menuButton =
        document.getElementById("mobileMenuButton");

    const mobileNavigation =
        document.getElementById("mobileNavigation");

    const siteHeader =
        document.querySelector(".site-header");


    /* =========================================
       CHECK ELEMENTS
    ========================================= */

    console.log("Menu button:", menuButton);
    console.log("Mobile navigation:", mobileNavigation);


    /* =========================================
       MOBILE MENU
    ========================================= */

    if (menuButton && mobileNavigation) {

        menuButton.addEventListener("click", function () {

            console.log("Mobile menu button clicked");

            const isOpen =
                mobileNavigation.classList.contains("open");


            if (isOpen) {

                mobileNavigation.classList.remove("open");

                menuButton.classList.remove("active");

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

                console.log("Mobile menu CLOSED");

            } else {

                mobileNavigation.classList.add("open");

                menuButton.classList.add("active");

                menuButton.setAttribute(
                    "aria-expanded",
                    "true"
                );

                console.log("Mobile menu OPENED");

            }

            console.log(
                "Navigation class:",
                mobileNavigation.className
            );

        });


        /* =====================================
           CLOSE MENU AFTER LINK CLICK
        ===================================== */

        const mobileLinks =
            mobileNavigation.querySelectorAll("a");


        mobileLinks.forEach(function (link) {

            link.addEventListener("click", function () {

                /*
                 * Don't close WhatsApp unnecessarily.
                 * Normal navigation links close the menu.
                 */

                if (
                    !link.classList.contains(
                        "mobile-whatsapp"
                    )
                ) {

                    mobileNavigation.classList.remove(
                        "open"
                    );

                    menuButton.classList.remove(
                        "active"
                    );

                    menuButton.setAttribute(
                        "aria-expanded",
                        "false"
                    );

                }

            });

        });

    } else {

        console.error(
            "Mobile menu elements were NOT found."
        );

    }


    /* =========================================
       HEADER SCROLL EFFECT
    ========================================= */

    if (siteHeader) {

        function handleHeaderScroll() {

            if (window.scrollY > 20) {

                siteHeader.classList.add(
                    "scrolled"
                );

            } else {

                siteHeader.classList.remove(
                    "scrolled"
                );

            }

        }


        window.addEventListener(
            "scroll",
            handleHeaderScroll
        );


        handleHeaderScroll();

    }

});