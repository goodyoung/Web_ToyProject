from django.shortcuts import render
from django.http import HttpResponse

def vote(request):
    return HttpResponse("안녕하세요 vote에 오신것을 환영합니다.")