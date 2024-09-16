from django import forms
from django.contrib.auth.forms import UserCreationForm

from taxi.models import Driver


class DriverCreationForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = (
            "username",
            "first_name",
            "last_name",
            "license_number",
            "password1",
            "password2"
        )

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise forms.ValidationError(
                "he license number must be 8 characters long."
            )
        if (
                not license_number[:3].isalpha()
                or not license_number[:3].isupper()
        ):
            raise forms.ValidationError(
                "The first 3 characters must be capital letters."
            )
        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "The last 5 characters must be numbers."
            )

        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise forms.ValidationError(
                "The license number must be 8 characters long.")

        if (
                not license_number[:3].isalpha()
                or not license_number[:3].isupper()
        ):
            raise forms.ValidationError(
                "The first 3 characters must be capital letters."
            )

        if not license_number[3:].isdigit():
            raise forms.ValidationError(
                "The last 5 characters must be numbers."
            )

        return license_number
