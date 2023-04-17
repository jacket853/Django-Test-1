from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # adding a name this time
]
