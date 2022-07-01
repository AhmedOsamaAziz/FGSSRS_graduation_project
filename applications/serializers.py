from dataclasses import fields
from rest_framework import serializers
from applications.models import Application



class Applicationseializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'



