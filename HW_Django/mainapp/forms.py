from django.forms import ModelForm

from mainapp.models import Owner
from mainapp.models import Pet


class OwnerFormAdmin(ModelForm):
    model = Owner,
    fields = ['first_name', 'last_name', 'city', 'purpose']


class PetFormAdmin(ModelForm):
    model = Pet,
    fields = ['breed', 'nickname', 'age', 'sex', 'owner']
