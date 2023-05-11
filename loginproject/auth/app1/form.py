from django import forms
from app1.models import auth
from app1.models import CustomUser
from app1.models import Employee
from django.contrib.auth.forms import UserCreationForm


class authForm(forms.ModelForm):
    class Meta:
        model=auth
        fields='__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phno','address')

    

class employeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'