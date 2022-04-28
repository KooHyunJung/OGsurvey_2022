from django.shortcuts import render, redirect
from survey_q.models import Question, Choice
from survey_a.models import Participant, Answer

# Create your views here.
def send_survey_detail(request, pk):
    if request.method == 'GET':
        survey = Question.objects.filter(id=pk)
        return render(request, "survey_q/survey_detail.html", { 'survey': survey })