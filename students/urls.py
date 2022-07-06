from django.urls import path
from . import views

urlpatterns = [
    path('student_list',  views.Student_List.as_view()), 
    path('student_pk/<int:pk>',  views.Student_PK.as_view()), 
    path('studyspecialize_list',  views.StudySpecialize_List.as_view()),
    path('studytype_list',  views.StudyType_List.as_view()),
]