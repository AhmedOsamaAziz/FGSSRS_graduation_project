from dataclasses import fields
from rest_framework import serializers
from generic.models import Person

class Personseializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'