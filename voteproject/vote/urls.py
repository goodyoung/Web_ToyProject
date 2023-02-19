from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('', views.vote, name='voteselect'),
    path('voting/<int:titled_id>/',views.voting, name = 'voting'),
]