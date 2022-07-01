from django.shortcuts import render
from urllib import response
from django.http.response import JsonResponse 
from .models import Person
from rest_framework.decorators import api_view
from .serializers import Personseializers   
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework import generics #, mixins, viewsets 

class Person_List(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset=Person.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Personseializers

class Person_PK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset=Person.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Personseializers

# # Create your views here.
# @api_view(['GET','POST'])            #Name this decorator
# def FBV_List(request):
#     #Get
#     if request.method == 'GET':
#         guests = Person.objects.all()
#         serializers = Personseializers(guests, many =True )
#         return Response(serializers.data)
#     #post    
#     elif request.method == 'POST':
#         serializers = Personseializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

# # #3.2 GUT put Delete
# @api_view()
# def FBV_pk(request , pk):
#     #GET
#         if request.method == 'Get':
#             guests = Person.objects.all()
#             serializers = Personseializers(guests, many =True )
#             return response(serializers.data)
#     #put    
#         elif request.method == 'PUT':
#             serializers = Personseializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#             return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
#     #DELETE    
#         elif request.method == 'DELETE':

#             serializers = Personseializers(data = request.data)

#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)



# # Create your views here.
