from django import forms


class LoginForm(forms.Form):
    body = forms.CharField(required=True)
