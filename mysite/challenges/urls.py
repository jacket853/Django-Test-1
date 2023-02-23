from django.urls import path
from . import views


#tells use what functions to run when the user/client hits a specified URL

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_goal_by_num),
    path("<str:month>", views.monthly_goal)
]
