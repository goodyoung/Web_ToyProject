from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('signUp/', views.signUp, name='signUp'),
    path('logIn/', auth_views.LoginView.as_view(template_name='user/logIn.html'), name='logIn'),
    path('logOut/', auth_views.LogoutView.as_view(), name='logOut'),   
]