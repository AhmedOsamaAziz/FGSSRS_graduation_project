from django.shortcuts import render
from urllib import response
from django.http.response import JsonResponse 
from .models import Application
from rest_framework.decorators import api_view
from .serializers import  Applicationseializers
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework import generics #, mixins, viewsets 




class Application_List(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset=Application.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Applicationseializers

class Application_PK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset=Application.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Applicationseializers

