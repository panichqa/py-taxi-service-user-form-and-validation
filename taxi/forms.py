from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from taxi.models import Driver, Car


validate_license_number = RegexValidator(
    regex=r'^[A-Z]{3}\d{5}$',
    message="The license number must consist of 3 capital letters followed by 5 numbers."
)


class LicenseNumberValidationForm(forms.ModelForm):
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        validate_license_number(license_number)
        return license_number


class DriverCreationForm(UserCreationForm, LicenseNumberValidationForm):
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


class DriverLicenseUpdateForm(LicenseNumberValidationForm):
    class Meta:
        model = Driver
        fields = ("license_number", )


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("model", "manufacturer", "drivers")

    drivers = forms.ModelMultipleChoiceField(
        queryset=Driver.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Add Drivers"
    )
