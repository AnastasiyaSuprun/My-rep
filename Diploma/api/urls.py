from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import OwnersList
from .views import PetsList
from .views import SheltersList
from .views import OwnerDetail
from .views import PetDetail
from .views import ShelterDetail


urlpatterns = [
    path('ownerslist/', OwnersList.as_view()),
    path('ownerslist/<int:pk>/', OwnerDetail.as_view()),
    path('petslist/', PetsList.as_view()),
    path('petslist/<int:pk>/', PetDetail.as_view()),
    path('shelterslist/', SheltersList.as_view()),
    path('shelterslist/<int:pk>/', ShelterDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
