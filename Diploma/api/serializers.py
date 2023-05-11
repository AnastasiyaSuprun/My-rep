from mainapp.models import Owner
from mainapp.models import Pet
from mainapp.models import Shelter
from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'city']


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'breed', 'nickname', 'age', 'sex']


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['id', 'title', 'manager', 'city']
