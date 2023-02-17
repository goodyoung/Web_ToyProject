from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from main.models import Registration_title
from .form import TitleForm,ArticleForm

def vote(request):
    if request.method == 'POST':
        # form = TitleForm(request.POST).     form은 나중에 사용하자~!~!~!
        vote_title = request.POST['vote']
        print(vote_title)
        ## vote_title을 전달하자~!~!~!~!~!~!~!~!
        return redirect('vote:voting')
    context = {'vote_title': Registration_title.objects.all()}
    return render(request, 'vote/vote_select.html', context)

def voting(request):
    return HttpResponse('안녕하세요 voting page입니다.')