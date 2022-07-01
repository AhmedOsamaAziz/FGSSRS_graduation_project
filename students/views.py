from django.shortcuts import render
from urllib import response
from django.http.response import JsonResponse 
from .models import Student
from rest_framework.decorators import api_view
from .serializers import  Studentseializers   
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework import generics #, mixins, viewsets 




class Student_List(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset=Student.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Studentseializers

class Student_PK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset=Student.objects.all()
    # Must be named 'serializer_class'
    serializer_class=Studentseializers



# # Create your views here.
# @api_view(['GET','POST'])            #Name this decorator
# def FBV_List(request):
#     #Get
#     if request.method == 'GET':
#         guests = Student.objects.all()
#         serializers = Studentseializers(guests, many =True )
#         return Response(serializers.data)
#     #post    
#     elif request.method == 'POST':
#         serializers = Studentseializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

# # #3.2 GUT put Delete
# @api_view()
# def FBV_pk(request , pk):
#     #GET
#         if request.method == 'Get':
#         guests = Person.objects.all()
#         serializers = Studentseializers(guests, many =True )
#         return response(serializers.data)
#     #put    
#     elif request.method == 'PUT':
#         serializers = Studentseializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
#     #DELETE    
#     elif request.method == 'DELETE':
#         serializers = Studentseializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status= status.HTTP_201_CREATED)
#         return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

