from django.urls import path
from friends.views import *
urlpatterns = [


    path('addfriend', addfriend ,name="addfriend_url"),
    path('get_myfriends', get_myfriends ,name="get_myfriends_url"),




]
