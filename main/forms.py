from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """Signup form with email and polished field styling."""

    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "you@example.com"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Choose a username"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "password1": "Create a strong password",
            "password2": "Confirm your password",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.setdefault("class", "auth-input")
            if field_name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[field_name]
