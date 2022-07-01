from django.urls import path
from . import views

urlpatterns = [
    path('applications_list',  views.Application_List.as_view()), 
    path('applications_pk/<int:pk>',  views.Application_PK.as_view()), 
]