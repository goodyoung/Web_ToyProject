from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from main.models import Registration_title, Registration_article
from .form import TitleForm, ArticleForm

def vote(request):
    if request.method == 'POST':
        # form = TitleForm(request.POST).     form은 나중에 사용하자~!~!~!
        vote_title = request.POST['vote']
        print(vote_title)
        titled = Registration_title.objects.get(title = vote_title)
        return redirect('vote:voting', titled_id = titled.id)  # id 왜 오류나지 --> model에 id가 없어서 그렇다.

    context = {'vote_title': Registration_title.objects.all()}
    return render(request, 'vote/vote_select.html', context)

def voting(request, titled_id):
    if request.method == 'POST':
        voting_result = request.POST['votings']
        print('voting결과: ', voting_result)
        ## voting결과까진 뽑혔다.. 이제 count추가
        return render(request, 'main/main.html')  #redirect로 변경 가능?
    #titled_id에 맞는 article만 가져온다.
    articles = Registration_article.objects.filter(registration_id = titled_id).values_list('article',
                                                                                            flat = True)
    context = {'votings': articles}
    return render(request, 'vote/voting.html', context)
    # return HttpResponse('안녕하세요 voting page입니다.')