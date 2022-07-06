from django.urls import path
from . import views

urlpatterns = [
    path('applications_list',  views.ApplicationList.as_view()),
    path('pickup/<int:application_id>', views.pickup_application),
    path('picked_applications_list',  views.get_available_applications),
    path('applications_pk/<int:pk>', views.ApplicationPK.as_view()),
    path('cyclestagelink_list', views.CycleStageLinkList.as_view()),
    path('cyclestagelink_pk/<int:pk>', views.CycleStageLinkPK.as_view()),
    path('cycle_list', views.CycleList.as_view()),
    path('cycle_pk/<int:pk>',  views.Cycle_PK.as_view()), 
    path('cyclestageroute_list', views.CycleStageRouteList.as_view()),
    path('cyclestageroute_pk/<int:pk>', views.CycleStageRoutePK.as_view()),
    path('login', views.validate_login),
    path('add_application_documnet', views.insert_application_document),
    path('postponed_course', views.PostponedCourseList.as_view()),
    path('get_next_route_of/<int:cycle_id>', views.get_next_route_of)
]