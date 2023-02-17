from django.shortcuts import render
from django.http import HttpResponse

def vote(request):
    return render(request, 'vote/vote_select.html')