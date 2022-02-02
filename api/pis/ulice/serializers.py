from dataclasses import field
from rest_framework import serializers
from .models import Ulica

class UlicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ulica
        fields=['ulica']