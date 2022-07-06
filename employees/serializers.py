from dataclasses import fields
from rest_framework import serializers
from employees.models import Employee

class Employeeseializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'emp_name',
            'email',
            'mobile',
            'national_id'
            ]