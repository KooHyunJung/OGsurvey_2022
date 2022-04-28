from django import forms
from survey_q.models import Question, Choice


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "notice"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["user_name"].label = "이름(배송 받으실 분)"
    #     self.fields["email"].label = "이메일"
    #     self.fields["address"].label = "배송 주소"
    #     self.fields["postal_code"].label = "우편 번호"

class ChoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["category", "choice_title", "item1","item2","item3","item4","item5","item6"]
