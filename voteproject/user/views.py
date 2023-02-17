from django.http import HttpResponse
from django.shortcuts import render
from main.models import UserInfo, Proposal, Registration_title, Registration_article

def signUp(request):
    return render(request,'user/signUp.html')

def logIn(request):
    return render(request,'user/logIn.html')

def logOut(request):
    return render(request,'user/logOut.html')

