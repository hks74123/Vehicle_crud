from django.contrib import admin
from django.urls import path
from hks.views import home,add_veh,add_vehicle,showdetails,notification_test_page,update_vehicle,show_up,delete_vehicle

urlpatterns = [ 
    path('',home.as_view()),
    path('add_form/',add_veh.as_view()),
    path('add_vehicle/',add_vehicle.as_view()),
    path('show_details/<int:pk>/',showdetails.as_view()),
    path('notifications/',notification_test_page.as_view()),
    path('update_vehicle/<int:pk>/',update_vehicle.as_view()),
    path('shupd/',show_up.as_view()),
    path('delete_vehicle/<int:pk>/',delete_vehicle.as_view()),
]
  