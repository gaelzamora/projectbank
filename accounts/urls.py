from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register')
]