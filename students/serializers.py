from dataclasses import fields
from rest_framework import serializers
from students.models import Student



class Studentseializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


