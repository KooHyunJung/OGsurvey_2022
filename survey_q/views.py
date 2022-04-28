from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from survey_q.models import Question, Choice
from survey_q.forms import QuestionUpdateForm, ChoiceUpdateForm


# Create your views here.
@login_required(login_url='user:login')
def survey_create(request):
    writer = request.user.id
    if request.method == 'GET':
        return render(request, "survey_q/survey_create.html")
    elif request.method == 'POST':
        title = request.POST.get("title", None)
        notice = request.POST.get("notice", None)
        choice_title = request.POST.get("choice_title", None)
        category = request.POST.get("category", None)
        item1 = request.POST.get("item1", None)
        item2 = request.POST.get("item2", None)
        item3 = request.POST.get("item3", None)
        item4 = request.POST.get("item4", None)
        item5 = request.POST.get("item5", None)
        item6 = request.POST.get("item6", None)

        question = Question.objects.create(writer_id=writer, title=title, notice=notice)
        Choice.objects.create(question_id=question.id, choice_title=choice_title, category=category, item1=item1, item2=item2, item3=item3, item4=item4, item5=item5, item6=item6)

        return redirect("survey_a:detail", question.id)


@login_required(login_url='user:login')
def survey_list(request):
    if request.method == 'GET':
        SurveyList = Question.objects.all().order_by('-id')
        return render(request, "survey_q/survey_list.html", { 'list': SurveyList })
    elif request.method == 'POST':
        return redirect("survey_q:create")


@login_required(login_url='user:login')
def survey_information(request, pk):
    if request.method == 'GET':
        survey = Question.objects.filter(id=pk)
        return render(request, "survey_q/survey_info.html", { 'survey': survey })


@login_required(login_url='user:login')
def survey_update(request, pk):
    question = Question.objects.get(id=pk)
    # choice = Choice.objects.filter(question_id=pk) # Question 연결된 Choice는 다중이라 오류 발생
    if request.method == 'POST':
        form1 = QuestionUpdateForm(request.POST)
        # form2 = ChoiceUpdateForm(request.POST)
        if form1.is_valid():
            question.title = request.POST["title"]
            question.notice = request.POST["notice"]
            question.save()
        # if form2.is_valid():
        #     choice.category = request.POST["category"]
        #     choice.choice_title = request.POST["choice_title"]
        #     choice.item1 = request.POST["item1"]
        #     choice.item2 = request.POST["item2"]
        #     choice.item3 = request.POST["item3"]
        #     choice.item4 = request.POST["item4"]
        #     choice.item5 = request.POST["item5"]
        #     choice.item6 = request.POST["item6"]
        #     choice.save()
        return redirect("survey_a:detail", pk=pk)
    elif request.method == 'GET':
        questionD = QuestionUpdateForm(instance = question)
        context1 = {"question": questionD}
        # choiceD = ChoiceUpdateForm(instance = choice.id)
        # context2 = {"choice": choiceD}
        return render(request, "survey_q/survey_update.html", context1)


@login_required(login_url='user:login')
def survey_delete(request, pk):
    Question.objects.filter(id=pk).delete()
    return redirect("survey_q:list")