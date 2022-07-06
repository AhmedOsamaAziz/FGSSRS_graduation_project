from os import stat
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .models import Application, Cycle, Cycle_Stage_Link, CycleStageRoute, PostponeCourseDocument
from .serializers import Applicationseializers, CycleStageLinkSerializer, CycleSerializer, CycleStageRouteSerializer, \
    PostponeCourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from students.models import Student
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse


class ApplicationList(generics.ListCreateAPIView):
    # Must be named 'queryset'
    # queryset=Application.objects.all()
    # Must be named 'serializer_class'
    serializer_class = Applicationseializers

    def get_queryset(self):
        queryset = Application.objects.filter(current_employee_id=None)
        # employee = self.request.query_params.get('current_employee_id')
        # if employee is not None:
        #     queryset = queryset.filter(current_employee_id=employee)
        return queryset


@api_view(['GET'])
def get_available_applications(request):
    employee_id = request.query_params.get('current_employee_id')
    picked_applications = Application.objects.filter(current_employee_id=employee_id)
    serializer = Applicationseializers(picked_applications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationPK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset = Application.objects.all()
    # Must be named 'serializer_class'
    serializer_class = Applicationseializers


class CycleStageLinkList(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset = Cycle_Stage_Link.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleStageLinkSerializer


class CycleStageLinkPK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset = Cycle_Stage_Link.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleStageLinkSerializer


class CycleList(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset = Cycle.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleSerializer


class Cycle_PK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset = Cycle.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleSerializer


class CycleStageRouteList(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset = CycleStageRoute.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleStageRouteSerializer


class CycleStageRoutePK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset = CycleStageRoute.objects.all()
    # Must be named 'serializer_class'
    serializer_class = CycleStageRouteSerializer


@api_view(['PUT'])
def pickup_application(request, application_id):
    try:
        application = Application.objects.get(pk=application_id)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Applicationseializers(application, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def validate_login(request):
    username = request.query_params.get('user_name')
    password = request.query_params.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class PostponedCourseList(generics.ListCreateAPIView):
    # Must be named 'queryset'
    queryset = PostponeCourseDocument.objects.all()
    # Must be named 'serializer_class'
    serializer_class = PostponeCourseSerializer


class PostponedCoursePK(generics.RetrieveUpdateDestroyAPIView):
    # Must be named 'queryset'
    queryset = PostponeCourseDocument.objects.all()
    # Must be named 'serializer_class'
    serializer_class = PostponeCourseSerializer


@api_view(['POST'])
def insert_application_document(request):

    application = Application()
    application.application_number = request.data['application_number']
    application.current_cycle_stage_link_id = Cycle_Stage_Link.objects.get(id=request.data['current_cycle_stage_link_id'])
    application.student_id = Student.objects.get(id=request.data['student_id'])
    application.save()

    if application.id is not None:
        document = PostponeCourseDocument()
        document.application_id = application
        document.subject_name = request.data['subject_name']
        document.postpone_reason = request.data['postpone_reason']
        document.save()

        serializer = PostponeCourseSerializer(document)

        if document.id is not None:
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['GET'])
def get_next_route_of(request, cycle_id):
    route = CycleStageRoute.objects.filter(cycle_stage_link_id=cycle_id)

    serializer = CycleStageRouteSerializer(route, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
