from django.db import models
from survey_q.models import Question, Choice
from django.core.validators import RegexValidator


# 사용자 모델 Participant, Answer
class Participant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$') # 전화번호 필드 유효성검사
    phone = models.CharField(validators = [phoneNumberRegex], max_length = 16, verbose_name="작성자 전화번호")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")

class Answer(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, verbose_name="설문 작성자")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name="설문 질문 항목")
    num = models.IntegerField(verbose_name="설문 질문 응답")