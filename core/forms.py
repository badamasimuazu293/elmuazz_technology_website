from django import forms

from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):

    class Meta:

        model = ContactInquiry

        fields = [
            "name",
            "company",
            "email",
            "phone",
            "service",
            "budget",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "class": "form-control",
                }
            ),

            "company": forms.TextInput(
                attrs={
                    "placeholder": "Company or organization",
                    "class": "form-control",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "class": "form-control",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+234 800 000 0000",
                    "class": "form-control",
                }
            ),

            "service": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "budget": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder":
                        "Tell us about your project...",
                    "class": "form-control",
                    "rows": 6,
                }
            ),
        }

class ContactReplyForm(forms.Form):

    reply = forms.CharField(
        label="Reply Message",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 10,
                "placeholder": "Write your reply to the customer...",
            }
        )
    )