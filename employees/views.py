from django.shortcuts import render
from urllib import response
from django.http.response import JsonResponse 
from .models import Employee #, Person
from rest_framework.decorators import api_view
from .serializers import Employeeseializers #, Personseializers   
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework import generics #, mixins, viewsets 



class Employee_List(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset=Employee.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Employeeseializers

class Employee_PK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset=Employee.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Employeeseializers
