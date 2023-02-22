from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import urls
from . import views
from .views import Register_serializer
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api',Register_serializer)

urlpatterns = [
    path('', views.main),   
    # path('api-auth/', include(urls)
    # path('api-view/', Register_serializer.as_view({'get':'list', 'put':'create'}))
    path('',include(router.urls))
]
#
 