"""
superlists URL Configuration
"""
from django.urls import path, include
from lists.views import home_page, new_list

urlpatterns = [
    path('', home_page, name='home'),
    path('lists/', include('lists.urls')),
]
