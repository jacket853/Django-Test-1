from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<str:money_type>", views.money_target)
    # path("<int:currency>", views.currency_types)
]