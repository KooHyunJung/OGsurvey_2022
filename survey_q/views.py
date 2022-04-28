from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from survey_q.models import Question


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
        SurveyList = Question.objects.all().order_by('-id')
        return render(request, "survey_q/survey_list.html", { 'list': SurveyList })
    elif request.method == 'POST':
        return redirect("survey_q:create")

@login_required
def survey_information(request, pk):
    if request.method == 'GET':
        survey = Question.objects.filter(id=pk)
        return render(request, "survey_q/survey_info.html", { 'survey': survey })