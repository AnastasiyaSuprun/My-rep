from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .utils import paginate
from .models import Owner
from .models import Pet
from .models import Shelter

menu = [
    {'title': 'Home', 'url': '/'},
    {'title': 'Owners', 'url': '/owners-list'},
    {'title': 'Pets', 'url': '/pets-list'},
    {'title': 'Shelters', 'url': '/shelters-list'},
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Pet Match',
    }
    return render(request, 'index.html', context)


def owners_list(request):
    owners = Owner.objects.all()
    context = {
        'menu': menu,
        'title': 'Pet Match | Owners',
    }
    context = paginate(owners, 3, request, context, var_name='owners')

    return render(request, 'owners_list.html', context)


def pets_list(request):
    pets = Pet.objects.all()
    context = {
        'menu': menu,
        'title': 'Pet Match | Pets',
    }
    context = paginate(pets, 3, request, context, var_name='pets')

    return render(request, 'pets_list.html', context)


def shelters_list(request):
    context = {
        'menu': menu,
        'title': 'Pet Match | Shelters',
        'shelters': Shelter.objects.all(),
    }

    return render(request, 'shelters_list.html', context)

