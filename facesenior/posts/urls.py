from django.urls import path
from posts.views import *
urlpatterns = [


    path('addpost', addpost ,name="addpost_url"),
    path('getpost', get_all  ,name="getpost_url"),
    path('getmypost', get_mypost, name="getmypost_url"),
    path('<int:post_id>/delete', get_delete),
    path('<int:post_id>/edit', get_edit , name="editpost_url"),


]
