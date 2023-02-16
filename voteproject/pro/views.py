from django.shortcuts import render
from django.http import HttpResponse

def pro(request):
    return HttpResponse("안녕하세요 pro에 오신것을 환영합니다.")