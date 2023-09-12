from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.transfer, name="transfer"),
    path('preview/', views.search_account, name="search_account"),
]
