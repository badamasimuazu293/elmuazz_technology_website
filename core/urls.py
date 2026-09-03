from django.urls import path
from . import views


app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("emcare/", views.emcare, name="emcare"),
    path("contact/", views.contact, name="contact"),
path(
    "contact/success/",
    views.contact_success,
    name="contact_success"
),
path(
    "services/<slug:slug>/",
    views.service_detail,
    name="service_detail"
),

path(
    "admin-dashboard/",
    views.dashboard,
    name="dashboard",
),

path(
    "admin-dashboard/inquiries/",
    views.dashboard_inquiries,
    name="dashboard_inquiries",
),
path(
    "admin-dashboard/inquiries/<int:inquiry_id>/",
    views.dashboard_inquiry_detail,
    name="dashboard_inquiry_detail",
),
    path(
        "dashboard/inquiries/<int:inquiry_id>/status/",
        views.dashboard_inquiry_status,
        name="dashboard_inquiry_status",
    ),

    path(
        "dashboard/inquiries/<int:inquiry_id>/reply/",
        views.dashboard_inquiry_reply,
        name="dashboard_inquiry_reply",
    ),
    

path(
    "admin-login/",
    views.dashboard_login,
    name="dashboard_login",
),

path(
    "admin-logout/",
    views.dashboard_logout,
    name="dashboard_logout",
),

]