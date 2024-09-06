from django.forms import forms
from .models import Register
class RegisterForm(forms.Form):
    class Meta:
        model=Register
        fields='__all__'
        label={'cfmpwd':'Confirm Password'}
