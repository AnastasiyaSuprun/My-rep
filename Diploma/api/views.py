from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from mainapp.models import Owner
from mainapp.models import Pet
from mainapp.models import Shelter

from .serializers import OwnerSerializer
from .serializers import PetSerializer
from .serializers import ShelterSerializer

from .paginations import OwnerPagination
from .paginations import PetPagination
from .paginations import ShelterPagination


class OwnersList(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['last_name', 'first_name', 'city']
    search_fields = ['last_name', 'city']
    pagination_class = OwnerPagination


class PetsList(ListAPIView):
    queryset = Pet.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['breed', 'nickname', 'age']
    search_fields = ['breed', 'nickname']
    serializer_class = PetSerializer
    pagination_class = PetPagination


class SheltersList(ListAPIView):
    queryset = Shelter.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['city', 'title']
    search_fields = ['city', 'title', 'manager']
    serializer_class = ShelterSerializer
    pagination_class = ShelterPagination


class OwnerDetail(RetrieveAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class PetDetail(RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class ShelterDetail(RetrieveAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
