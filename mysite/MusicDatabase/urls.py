from django.urls import path
from . import views

# tell our server what functions to run when user this specified url

urlpatterns = [
    path("", views.index),
]
