from django import forms
from kiosk.models import User


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    DOB = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )

    class Meta():
        model= User
        fields='__all__'
