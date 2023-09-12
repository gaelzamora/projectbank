from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('', views.wallet, name="wallet"),
    path('my_transfers/', views.my_transfer, name="myTransfers")
]   