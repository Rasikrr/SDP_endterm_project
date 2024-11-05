from collections import OrderedDict

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from users.models import CustomUser


class FormFactory:
    @staticmethod
    def create_form(form_type, *args, **kwargs):
        if form_type == "login":
            return LoginForm(*args, **kwargs)
        elif form_type == "signup":
            return CreateUserForm(*args, **kwargs)
        elif form_type == "profile":
            return ProfileForm(*args, **kwargs)
        else:
            raise ValueError(f"Unknown form type: {form_type}")


class LoginForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def validate_unique(self):
        pass


class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


class ProfileForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("image", "first_name", "last_name", "username", "email")
