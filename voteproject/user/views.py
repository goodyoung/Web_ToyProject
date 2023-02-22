# from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from user.form import UserInfoForm

def signUp(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            #raw_pass = make_password(form.cleaned_data.get('password'))
            # user = authenticate(username=username, password=raw_password)  # 사용자 인증
            # login(request, user)  # 로그인
            return redirect('main')
        render(request, 'main/main.html')
    else:
        form = UserInfoForm()
    return render(request, 'user/signUp.html', {'form': form})
