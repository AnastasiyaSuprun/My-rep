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


# from django.contrib.auth import authenticate
# from rest_framework import serializers
# from .models import User
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True,
#     )
#
#     token = serializers.CharField(
#         max_length=255,
#         read_only=True,
#     )
#
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'token']
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
#
# class LoginSerializer(serializers.ModelSerializer):
#
#     email = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255, read_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#
#         email = data.get('email', None)
#         password = data.get('password', None)
#
#         if email is None:
#             raise serializers.ValidationError(
#                 'An email address is required to log in.'
#             )
#
#         if password is None:
#             raise serializers.ValidationError(
#                 'A password is required to log in.'
#             )
#
#         user = authenticate(username=email, password=password)
#
#         if user is None:
#             raise serializers.ValidationError(
#                 'A user with this email and password was not found.'
#             )
#
#         if not user.is_active:
#             raise serializers.ValidationError(
#                 'This user has been deactivated.'
#             )
#
#         return {
#             'email': user.email,
#             'username': user.username,
#             'token': user.token
#         }
#
