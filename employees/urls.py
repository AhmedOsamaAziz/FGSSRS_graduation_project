from django.urls import path
from . import views

urlpatterns = [
    path('employees_list',  views.Employee_List.as_view()), 
    path('employees_pk/<int:pk>',  views.Employee_PK.as_view()), 
]