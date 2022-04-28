from django import forms
from survey_q.models import Question, Choice


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "notice"]

class ChoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["category", "choice_title", "item1","item2","item3","item4","item5","item6"]
