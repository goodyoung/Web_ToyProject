from django.http import HttpResponse
from django.shortcuts import render
# from .models import 

def signUp(request):
    return HttpResponse("안녕하세요 signUp에 오신것을 환영합니다.")

def logIn(request):
    return HttpResponse("안녕하세요 logIn에 오신것을 환영합니다.")

def logOut(request):
    return HttpResponse("안녕하세요 logOut에 오신것을 환영합니다.")
