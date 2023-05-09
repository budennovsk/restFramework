from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """ Сериализуем поля БД"""
    class Meta:
        model = Car
        fields = "__all__"
