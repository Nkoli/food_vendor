from django.contrib.auth import authenticate
from .models import User
from rest_framework import serializers


def create_user_account(email, password, name, **extra_fields):
    user = User.objects.create_user(
        email=email, password=password, name=name, **extra_fields
    )
    return user


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if not user:
        raise serializers.ValidationError("Invalid email or password.")
    return user
