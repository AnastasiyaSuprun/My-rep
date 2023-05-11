from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(max_length=40, required=False)
    city = forms.CharField(label='City')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
