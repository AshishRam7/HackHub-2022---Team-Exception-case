from importlib.resources import path
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('labs', views.labs, name='labs'),
]
