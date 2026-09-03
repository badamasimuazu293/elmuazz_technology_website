document.addEventListener("DOMContentLoaded", function () {

    // =====================================================
    // SIDEBAR TOGGLE
    // =====================================================

    const sidebar = document.querySelector(".sidebar");
    const sidebarToggle = document.querySelector(".sidebar-toggle");
    const overlay = document.querySelector(".sidebar-overlay");

    if (sidebarToggle) {
        sidebarToggle.addEventListener("click", function () {
            sidebar.classList.toggle("open");

            if (overlay) {
                overlay.classList.toggle("active");
            }
        });
    }

    if (overlay) {
        overlay.addEventListener("click", function () {
            sidebar.classList.remove("open");
            overlay.classList.remove("active");
        });
    }


    // =====================================================
    // MOBILE SIDEBAR
    // =====================================================

    const mobileMenuButton = document.querySelector(".mobile-menu-button");

    if (mobileMenuButton) {
        mobileMenuButton.addEventListener("click", function () {

            sidebar.classList.toggle("open");

            if (overlay) {
                overlay.classList.toggle("active");
            }

        });
    }


    // =====================================================
    // CLOSE SIDEBAR WHEN MENU LINK IS CLICKED
    // =====================================================

    const menuLinks = document.querySelectorAll(".menu-link");

    menuLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            if (window.innerWidth <= 768 && sidebar) {

                sidebar.classList.remove("open");

                if (overlay) {
                    overlay.classList.remove("active");
                }

            }

        });

    });


    // =====================================================
    // ACTIVE SIDEBAR LINK
    // =====================================================

    const currentPath = window.location.pathname;

    menuLinks.forEach(function (link) {

        const linkPath = new URL(
            link.href,
            window.location.origin
        ).pathname;

        if (
            linkPath === currentPath ||
            (
                linkPath !== "/" &&
                currentPath.startsWith(linkPath)
            )
        ) {
            link.classList.add("active");
        }

    });


    // =====================================================
    // USER DROPDOWN
    // =====================================================

    const userButton = document.querySelector(".admin-user");
    const userDropdown = document.querySelector(".user-dropdown");

    if (userButton && userDropdown) {

        userButton.addEventListener("click", function (event) {

            event.stopPropagation();

            userDropdown.classList.toggle("show");

        });

        document.addEventListener("click", function () {

            userDropdown.classList.remove("show");

        });

    }


    // =====================================================
    // DASHBOARD SEARCH
    // =====================================================

    const searchInput = document.querySelector(
        ".dashboard-search input"
    );

    const searchableRows = document.querySelectorAll(
        ".dashboard-table tbody tr"
    );

    if (searchInput && searchableRows.length) {

        searchInput.addEventListener("input", function () {

            const searchTerm = searchInput.value
                .toLowerCase()
                .trim();

            searchableRows.forEach(function (row) {

                const rowText = row.textContent
                    .toLowerCase();

                if (rowText.includes(searchTerm)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }

            });

        });

    }


    // =====================================================
    // AUTO DISMISS ALERTS
    // =====================================================

    const alerts = document.querySelectorAll(
        ".alert, .message, .dashboard-alert"
    );

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.classList.add("fade-out");

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 5000);

    });


    // =====================================================
    // CONFIRM DELETE / CLOSE ACTION
    // =====================================================

    const confirmButtons = document.querySelectorAll(
        "[data-confirm]"
    );

    confirmButtons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const message =
                button.dataset.confirm ||
                "Are you sure you want to continue?";

            if (!confirm(message)) {
                event.preventDefault();
            }

        });

    });


    // =====================================================
    // TABLE ROW CLICK
    // =====================================================

    const inquiryRows = document.querySelectorAll(
        ".dashboard-table tbody tr[data-url]"
    );

    inquiryRows.forEach(function (row) {

        row.addEventListener("click", function (event) {

            if (
                event.target.closest("a") ||
                event.target.closest("button")
            ) {
                return;
            }

            const url = row.dataset.url;

            if (url) {
                window.location.href = url;
            }

        });

    });


    // =====================================================
    // STATUS FILTER
    // =====================================================

    const statusFilter = document.querySelector(
        "#status-filter"
    );

    if (statusFilter) {

        statusFilter.addEventListener("change", function () {

            const selectedStatus =
                this.value.toLowerCase();

            const rows = document.querySelectorAll(
                ".dashboard-table tbody tr"
            );

            rows.forEach(function (row) {

                const statusBadge = row.querySelector(
                    ".status-badge"
                );

                if (!statusBadge) {
                    return;
                }

                const rowStatus =
                    statusBadge.textContent
                        .toLowerCase()
                        .trim();

                if (
                    selectedStatus === "" ||
                    rowStatus === selectedStatus
                ) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }

            });

        });

    }


    // =====================================================
    // CURRENT YEAR
    // =====================================================

    const yearElements = document.querySelectorAll(
        "[data-current-year]"
    );

    yearElements.forEach(function (element) {

        element.textContent =
            new Date().getFullYear();

    });


    // =====================================================
    // PREVENT DOUBLE FORM SUBMISSION
    // =====================================================

    const forms = document.querySelectorAll(
        "form[data-prevent-double-submit]"
    );

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const submitButton =
                form.querySelector(
                    'button[type="submit"], input[type="submit"]'
                );

            if (!submitButton) {
                return;
            }

            submitButton.disabled = true;

            const originalText =
                submitButton.textContent;

            submitButton.dataset.originalText =
                originalText;

            submitButton.textContent =
                "Processing...";

        });

    });


    // =====================================================
    // WINDOW RESIZE
    // =====================================================

    window.addEventListener("resize", function () {

        if (
            window.innerWidth > 768 &&
            sidebar &&
            overlay
        ) {

            sidebar.classList.remove("open");
            overlay.classList.remove("active");

        }

    });

});