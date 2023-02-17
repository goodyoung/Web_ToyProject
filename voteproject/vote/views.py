from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from main.models import Registration_title
def vote(request):
    print(Registration_title.objects.all())
    return render(request, 'vote/vote_select.html')