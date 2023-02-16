from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("안녕하세요 login에 오신것을 환영합니다.")
