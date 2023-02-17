from django.forms import ModelForm
from django.forms import TextInput
from django import forms
from mainapp.models import Owner
from mainapp.models import Pet


class OwnerFormAdmin(ModelForm):
    model = Owner,
    fields = ['first_name', 'last_name', 'city', 'purpose']


class PetFormAdmin(ModelForm):
    model = Pet,
    fields = ['breed', 'nickname', 'age', 'sex', 'owner']


class AddPetForm(ModelForm):
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    sex = forms.ChoiceField(choices=SEX_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner'].empty_label = 'Choose yourself'

    class Meta:
        model = Pet
        fields = ['breed', 'nickname', 'age', 'sex', 'photo', 'owner']

        widgets = {
            'breed': TextInput(attrs={
                'size': '30',
                'class': 'form-input',
            }),
            'nickname': TextInput(attrs={
                'size':  '20',
                'class': 'form-input',
            }),
            'age': TextInput(attrs={
                'size': '2',
                'class': 'form-input',
            }),
        }
