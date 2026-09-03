from django.contrib import admin, messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import path, reverse
from django.utils import timezone
from django.utils.html import format_html

from .models import ContactInquiry
from .forms import ContactReplyForm


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):

    # =====================================================
    # LIST VIEW
    # =====================================================

    list_display = (
        "status_badge",
        "name",
        "company",
        "email",
        "service",
        "budget",
        "created_at",
        "reply_button",
    )

    list_filter = (
        "status",
        "service",
        "budget",
        "created_at",
    )

    search_fields = (
        "name",
        "company",
        "email",
        "phone",
        "message",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "replied_at",
    )

    ordering = (
        "-created_at",
    )

    # =====================================================
    # DETAIL VIEW
    # =====================================================

    fieldsets = (

        (
            "Customer Information",
            {
                "fields": (
                    "name",
                    "company",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Project Information",
            {
                "fields": (
                    "service",
                    "budget",
                    "message",
                )
            },
        ),

        (
            "Inquiry Management",
            {
                "fields": (
                    "status",
                )
            },
        ),

        (
            "Reply Information",
            {
                "fields": (
                    "reply",
                    "replied_at",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    # =====================================================
    # CUSTOM ADMIN URL
    # =====================================================

    def get_urls(self):

        urls = super().get_urls()

        custom_urls = [
            path(
                "<int:inquiry_id>/reply/",
                self.admin_site.admin_view(
                    self.reply_view
                ),
                name="core_contactinquiry_reply",
            ),
        ]

        return custom_urls + urls

    # =====================================================
    # REPLY VIEW
    # =====================================================

    def reply_view(self, request, inquiry_id):

        inquiry = self.get_object(
            request,
            inquiry_id
        )

        if inquiry is None:

            self.message_user(
                request,
                "Contact inquiry not found.",
                level=messages.ERROR,
            )

            return redirect(
                "admin:core_contactinquiry_changelist"
            )

        if request.method == "POST":

            form = ContactReplyForm(
                request.POST
            )

            if form.is_valid():

                reply_message = form.cleaned_data[
                    "reply"
                ]

                # =========================================
                # SEND EMAIL TO CUSTOMER
                # =========================================

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

                # =========================================
                # SAVE REPLY
                # =========================================

                inquiry.reply = reply_message

                inquiry.replied_at = timezone.now()

                inquiry.status = "replied"

                inquiry.save(
                    update_fields=[
                        "reply",
                        "replied_at",
                        "status",
                        "updated_at",
                    ]
                )

                self.message_user(
                    request,
                    (
                        "Reply sent successfully to "
                        f"{inquiry.email}."
                    ),
                    level=messages.SUCCESS,
                )

                return redirect(
                    reverse(
                        "admin:core_contactinquiry_change",
                        args=[inquiry.id],
                    )
                )

        else:

            form = ContactReplyForm(
                initial={
                    "reply": inquiry.reply
                }
            )

        context = {
            **self.admin_site.each_context(request),

            "title": (
                f"Reply to {inquiry.name}"
            ),

            "inquiry": inquiry,

            "form": form,
        }

        return render(
            request,
            "admin/core/contactinquiry/reply.html",
            context,
        )

    # =====================================================
    # STATUS BADGE
    # =====================================================

    @admin.display(
        description="Status",
        ordering="status",
    )
    def status_badge(self, obj):

        badge_classes = {
            "new": "new",
            "read": "read",
            "in_progress": "progress",
            "replied": "replied",
            "closed": "closed",
        }

        labels = {
            "new": "New",
            "read": "Read",
            "in_progress": "In Progress",
            "replied": "Replied",
            "closed": "Closed",
        }

        css_class = badge_classes.get(
            obj.status,
            "read"
        )

        label = labels.get(
            obj.status,
            obj.get_status_display()
        )

        return format_html(
            '<span class="{}">{}</span>',
            f"status-badge status-{css_class}",
            label,
        )

    # =====================================================
    # REPLY BUTTON
    # =====================================================

    @admin.display(
        description="Action"
    )
    def reply_button(self, obj):

        url = reverse(
            "admin:core_contactinquiry_reply",
            args=[obj.id],
        )

        return format_html(
            '<a class="button" href="{}">Reply</a>',
            url,
        )