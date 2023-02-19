from django.contrib import admin
from django.urls import path, include
from main.views import main
app_name = 'mainpage'
urlpatterns = [
    path('', main, name='main'),
    path("admin/", admin.site.urls),
    path("user/", include('user.urls')),
    path("vote/", include('vote.urls')),
    path("pro/", include('pro.urls')),
]
