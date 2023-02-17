from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('signUp/', views.signUp, name='signUp'),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
]