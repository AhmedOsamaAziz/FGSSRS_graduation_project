from django.urls import path
from .import views



urlpatterns = [
    path('persons_list',views.Person_List.as_view()), 
    path('persons_pk/<int:pk>',views.Person_PK.as_view()), 
]