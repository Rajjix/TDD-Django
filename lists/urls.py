from django.urls import path, re_path
from . import views

app_name = 'lists'

urlpatterns = [
        path('new', views.new_list, name='new_list'),
        re_path(r'^(\d+)/$', views.view_list, name='view_list'),
        ]
