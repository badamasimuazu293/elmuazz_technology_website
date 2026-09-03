from django.db import models


class ContactInquiry(models.Model):

    SERVICE_CHOICES = [
        ("software", "Software Development"),
        ("web", "Web Development"),
        ("mobile", "Mobile App Development"),
        ("uiux", "UI/UX Design"),
        ("ai", "AI & Intelligent Systems"),
        ("automation", "Business Automation"),
        ("other", "Other"),
    ]

    BUDGET_CHOICES = [
        ("below-100k", "Below ₦100,000"),
        ("100k-300k", "₦100,000 – ₦300,000"),
        ("300k-500k", "₦300,000 – ₦500,000"),
        ("500k-1m", "₦500,000 – ₦1,000,000"),
        ("above-1m", "Above ₦1,000,000"),
        ("discuss", "Let's Discuss"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("read", "Read"),
        ("in_progress", "In Progress"),
        ("replied", "Replied"),
        ("closed", "Closed"),
    ]

    # =====================================================
    # CUSTOMER INFORMATION
    # =====================================================

    name = models.CharField(
        max_length=150
    )

    company = models.CharField(
        max_length=150,
        blank=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30
    )

    # =====================================================
    # PROJECT INFORMATION
    # =====================================================

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    budget = models.CharField(
        max_length=50,
        choices=BUDGET_CHOICES,
        blank=True
    )

    message = models.TextField()

    # =====================================================
    # INQUIRY MANAGEMENT
    # =====================================================

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    # =====================================================
    # REPLY INFORMATION
    # =====================================================

    reply = models.TextField(
        blank=True
    )

    replied_at = models.DateTimeField(
        null=True,
        blank=True
    )

    # =====================================================
    # TIMESTAMPS
    # =====================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.service}"

    def get_status_display_class(self):
        return self.status.replace("_", "-")