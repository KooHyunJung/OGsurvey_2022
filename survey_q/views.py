from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def survey_create(request):
    if request.method == 'GET':
        return render(request, "survey_q/survey_create.html")
    elif request.method == 'POST':
        return redirect("survey_q:list")

@login_required
def survey_list(request):
    if request.method == 'GET':
        # (코드 추가 예정)서비스 함수 생성, 관련 정보 내려주기
        return render(request, "survey_q/survey_list.html")
    elif request.method == 'POST':
        return redirect("survey_q:create")
        