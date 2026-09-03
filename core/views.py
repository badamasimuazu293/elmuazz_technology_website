
from django.shortcuts import render, redirect
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactInquiryForm


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def emcare(request):
    return render(request, "core/emcare.html")

def contact(request):

    if request.method == "POST":

        form = ContactInquiryForm(request.POST)

        if form.is_valid():

            inquiry = form.save()

            send_mail(
                subject="New Contact Request — Elmuazz Technology",

                message=f"""
A new contact request has been submitted through the
Elmuazz Technology website.

----------------------------------------
CUSTOMER INFORMATION
----------------------------------------

Name: {inquiry.name}
Company: {inquiry.company or "Not provided"}
Email: {inquiry.email}
Phone: {inquiry.phone}

Service: {inquiry.get_service_display()}
Budget: {
    inquiry.get_budget_display()
    if inquiry.budget
    else "Not specified"
}

----------------------------------------
MESSAGE
----------------------------------------

{inquiry.message}

----------------------------------------

Received:
{inquiry.created_at.strftime("%d %B %Y, %I:%M %p")}

Please log in to the Elmuazz Technology admin dashboard
to manage this inquiry.

Empowering Business with Technology.
""",

                from_email=None,

                recipient_list=[
                    settings.CONTACT_NOTIFICATION_EMAIL
                ],

                fail_silently=False,
            )

            return redirect(
                "core:contact_success"
            )

    else:

        form = ContactInquiryForm()

    return render(
        request,
        "core/contact.html",
        {
            "form": form
        }
    )

def contact_success(request):

    return render(
        request,
        "core/contact_success.html"
    )

# =====================================================
# SERVICE DETAILS
# =====================================================

SERVICES = {

    "custom-software-development": {
        "title": "Custom Software Development",

        "description": (
            "We build reliable and scalable software solutions "
            "designed around your unique business processes, "
            "operational needs, and long-term goals."
        ),

        "features": [
            {
                "title": "Business Management Systems",
                "description": (
                    "Custom systems that help businesses manage "
                    "their daily operations efficiently."
                ),
            },
            {
                "title": "Enterprise Applications",
                "description": (
                    "Secure and scalable applications designed "
                    "for organizations with complex requirements."
                ),
            },
            {
                "title": "Process Automation",
                "description": (
                    "Automate repetitive business processes and "
                    "reduce unnecessary manual work."
                ),
            },
            {
                "title": "System Integration",
                "description": (
                    "Connect your existing systems and services "
                    "to create a more unified digital workflow."
                ),
            },
        ],
    },


    "web-development": {
        "title": "Web Development",

        "description": (
            "We create modern, responsive, secure, and "
            "high-performing websites and web applications "
            "that help businesses establish a strong digital presence."
        ),

        "features": [
            {
                "title": "Business Websites",
                "description": (
                    "Professional websites that communicate "
                    "your brand and services effectively."
                ),
            },
            {
                "title": "Web Applications",
                "description": (
                    "Powerful browser-based applications built "
                    "around your business requirements."
                ),
            },
            {
                "title": "E-Commerce Solutions",
                "description": (
                    "Modern online platforms that help businesses "
                    "sell products and services digitally."
                ),
            },
            {
                "title": "Website Maintenance",
                "description": (
                    "Continuous improvements, updates, security, "
                    "and technical support for your website."
                ),
            },
        ],
    },


    "mobile-app-development": {
        "title": "Mobile App Development",

        "description": (
            "We develop user-friendly mobile applications that "
            "provide convenient, reliable, and powerful digital "
            "experiences."
        ),

        "features": [
            {
                "title": "Android Applications",
                "description": (
                    "Modern Android applications designed for "
                    "performance and usability."
                ),
            },
            {
                "title": "Business Mobile Apps",
                "description": (
                    "Mobile solutions that help organizations "
                    "serve customers and manage operations."
                ),
            },
            {
                "title": "Mobile User Experience",
                "description": (
                    "Simple and intuitive interfaces designed "
                    "for excellent mobile experiences."
                ),
            },
            {
                "title": "App Maintenance",
                "description": (
                    "Continuous updates, improvements, and "
                    "technical support for your application."
                ),
            },
        ],
    },


    "ui-ux-design": {
        "title": "UI/UX Design",

        "description": (
            "We design intuitive digital experiences that are "
            "simple, attractive, accessible, and enjoyable to use."
        ),

        "features": [
            {
                "title": "User Interface Design",
                "description": (
                    "Clean and professional interfaces designed "
                    "to communicate your brand effectively."
                ),
            },
            {
                "title": "User Experience Design",
                "description": (
                    "User-centered experiences that make digital "
                    "products easy and enjoyable to use."
                ),
            },
            {
                "title": "Wireframes & Prototypes",
                "description": (
                    "Interactive prototypes that allow ideas to "
                    "be tested before development."
                ),
            },
            {
                "title": "Design Systems",
                "description": (
                    "Consistent visual systems that help products "
                    "maintain a professional identity."
                ),
            },
        ],
    },


    "ai-intelligent-solutions": {
        "title": "AI & Intelligent Solutions",

        "description": (
            "We integrate artificial intelligence into software "
            "to automate tasks, analyze data, and support smarter "
            "business decisions."
        ),

        "features": [
            {
                "title": "AI-Powered Applications",
                "description": (
                    "Intelligent software solutions that use AI "
                    "to improve business processes."
                ),
            },
            {
                "title": "AI Chatbots & Assistants",
                "description": (
                    "Intelligent assistants that help businesses "
                    "communicate with customers and users."
                ),
            },
            {
                "title": "Predictive Analytics",
                "description": (
                    "Use data and machine learning to identify "
                    "patterns and support better decisions."
                ),
            },
            {
                "title": "Intelligent Automation",
                "description": (
                    "Automate repetitive tasks and workflows "
                    "using artificial intelligence."
                ),
            },
        ],
    },


    "digital-transformation": {
        "title": "Digital Transformation",

        "description": (
            "We help organizations move from manual processes "
            "to efficient, connected, and technology-driven "
            "digital workflows."
        ),

        "features": [
            {
                "title": "Business Process Digitization",
                "description": (
                    "Transform manual processes into efficient "
                    "digital workflows."
                ),
            },
            {
                "title": "Workflow Automation",
                "description": (
                    "Reduce repetitive work by automating "
                    "important business processes."
                ),
            },
            {
                "title": "Digital Strategy",
                "description": (
                    "Identify the right technologies and "
                    "strategies for your organization's growth."
                ),
            },
            {
                "title": "Technology Modernization",
                "description": (
                    "Improve existing systems and adopt modern "
                    "technology where it creates real value."
                ),
            },
        ],
    },

}



# =====================================================
# SERVICE DETAIL VIEW
# =====================================================

def service_detail(request, slug):

    service = SERVICES.get(slug)

    if service is None:
        raise Http404("Service not found.")

    return render(
        request,
        "core/service_detail.html",
        {
            "service": service,
        }
    )

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from .models import ContactInquiry


@staff_member_required
def dashboard(request):

    inquiries = ContactInquiry.objects.all()

    context = {
        "total_inquiries": inquiries.count(),

        "new_inquiries": inquiries.filter(
            status="new"
        ).count(),

        "in_progress_inquiries": inquiries.filter(
            status="in_progress"
        ).count(),

        "replied_inquiries": inquiries.filter(
            status="replied"
        ).count(),

        "closed_inquiries": inquiries.filter(
            status="closed"
        ).count(),

        "recent_inquiries": inquiries[:10],
    }

    return render(
        request,
        "core/dashboard/dashboard.html",
        context,
    )

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactInquiry


@staff_member_required

def dashboard_inquiries(request):

    inquiries = ContactInquiry.objects.all()

    context = {
        "inquiries": inquiries,

        "total_inquiries": inquiries.count(),

        "new_inquiries": inquiries.filter(
            status="new"
        ).count(),

        "in_progress_inquiries": inquiries.filter(
            status="in_progress"
        ).count(),

        "replied_inquiries": inquiries.filter(
            status="replied"
        ).count(),

        "closed_inquiries": inquiries.filter(
            status="closed"
        ).count(),
    }

    return render(
        request,
        "core/dashboard/inquiries.html",
        context,
    )

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render

from .models import ContactInquiry


@staff_member_required
def dashboard_inquiry_detail(request, inquiry_id):

    inquiry = get_object_or_404(
        ContactInquiry,
        id=inquiry_id
    )

    # Mark the inquiry as read when administrator opens it
    if not inquiry.is_read:
        inquiry.is_read = True

        if inquiry.status == "new":
            inquiry.status = "read"

        inquiry.save(
            update_fields=[
                "is_read",
                "status",
            ]
        )

    return render(
        request,
        "core/dashboard/inquiry_detail.html",
        {
            "inquiry": inquiry,
        }
    )

# =====================================================
# ELMUAZZ TECHNOLOGY DASHBOARD
# =====================================================

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .models import ContactInquiry


@login_required
def dashboard(request):
    inquiries = ContactInquiry.objects.all()

    context = {
        "total_inquiries": inquiries.count(),

        "new_inquiries": inquiries.filter(
            status="new"
        ).count(),

        "in_progress_inquiries": inquiries.filter(
            status="in_progress"
        ).count(),

        "replied_inquiries": inquiries.filter(
            status="replied"
        ).count(),

        "closed_inquiries": inquiries.filter(
            status="closed"
        ).count(),

        "recent_inquiries": inquiries[:10],
    }

    return render(
        request,
        "core/dashboard/dashboard.html",
        context,
    )

@login_required
def dashboard_inquiries(request):

    inquiries = ContactInquiry.objects.all()

    context = {
        "inquiries": inquiries,

        "total_inquiries": inquiries.count(),

        "new_inquiries": inquiries.filter(
            status="new"
        ).count(),

        "in_progress_inquiries": inquiries.filter(
            status="in_progress"
        ).count(),

        "replied_inquiries": inquiries.filter(
            status="replied"
        ).count(),

        "closed_inquiries": inquiries.filter(
            status="closed"
        ).count(),
    }

    return render(
        request,
        "core/dashboard/inquiries.html",
        context,
    )


@login_required
def dashboard_inquiry_detail(request, inquiry_id):

    inquiry = get_object_or_404(
        ContactInquiry,
        id=inquiry_id
    )

    # Automatically mark a new inquiry as read
    if inquiry.status == "new":

        inquiry.status = "read"

        inquiry.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

    context = {
        "inquiry": inquiry,

        "status_choices": (
            ContactInquiry.STATUS_CHOICES
        ),
    }

    return render(
        request,
        "core/dashboard/inquiry_detail.html",
        context,
    )


@login_required
def dashboard_inquiry_status(
    request,
    inquiry_id
):

    inquiry = get_object_or_404(
        ContactInquiry,
        id=inquiry_id
    )

    if request.method != "POST":

        return redirect(
            "core:dashboard_inquiry_detail",
            inquiry_id=inquiry.id,
        )

    status = request.POST.get("status")

    valid_statuses = dict(
        ContactInquiry.STATUS_CHOICES
    )

    if status not in valid_statuses:

        messages.error(
            request,
            "Invalid inquiry status.",
        )

        return redirect(
            "core:dashboard_inquiry_detail",
            inquiry_id=inquiry.id,
        )

    inquiry.status = status

    inquiry.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    messages.success(
        request,
        f"Inquiry status updated to {valid_statuses[status]}.",
    )

    return redirect(
        "core:dashboard_inquiry_detail",
        inquiry_id=inquiry.id,
    )


@login_required
def dashboard_inquiry_reply(
    request,
    inquiry_id
):

    inquiry = get_object_or_404(
        ContactInquiry,
        id=inquiry_id
    )

    if request.method != "POST":

        return redirect(
            "core:dashboard_inquiry_detail",
            inquiry_id=inquiry.id,
        )

    reply_message = request.POST.get(
        "reply",
        ""
    ).strip()

    if not reply_message:

        messages.error(
            request,
            "Please enter a reply before sending.",
        )

        return redirect(
            "core:dashboard_inquiry_detail",
            inquiry_id=inquiry.id,
        )

    # =================================================
    # SEND EMAIL
    # =================================================

    try:

        send_mail(

            subject=(
                "Re: Your Inquiry — "
                "Elmuazz Technology"
            ),

            message=f"""
Hello {inquiry.name},

Thank you for contacting Elmuazz Technology.

We have reviewed your inquiry regarding:

{inquiry.get_service_display()}

Our response is:

----------------------------------------

{reply_message}

----------------------------------------

If you have any additional questions,
please feel free to contact us.

Best regards,

Elmuazz Technology
Empowering Business with Technology.
""",

            from_email=None,

            recipient_list=[
                inquiry.email
            ],

            fail_silently=False,
        )

    except Exception:

        messages.error(
            request,
            "Unable to send the email. Please try again.",
        )

        return redirect(
            "core:dashboard_inquiry_detail",
            inquiry_id=inquiry.id,
        )

    # =================================================
    # SAVE REPLY
    # =================================================

    inquiry.reply = reply_message

    inquiry.status = "replied"

    from django.utils import timezone

    inquiry.replied_at = timezone.now()

    inquiry.save(
        update_fields=[
            "reply",
            "status",
            "replied_at",
            "updated_at",
        ]
    )

    messages.success(
        request,
        f"Reply successfully sent to {inquiry.email}.",
    )

    return redirect(
        "core:dashboard_inquiry_detail",
        inquiry_id=inquiry.id,
    )

from django.contrib.auth import logout
from django.shortcuts import redirect



def dashboard_login(request):

    if request.user.is_authenticated:
        return redirect("core:dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            if not user.is_staff:
                messages.error(
                    request,
                    "You do not have administrator access."
                )

                return redirect("core:dashboard_login")

            login(request, user)

            next_url = request.POST.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("core:dashboard")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "core/dashboard/login.html"
    )

@login_required
def dashboard_logout(request):

    logout(request)

    return redirect("core:dashboard_login")