from django.db import models
from django.contrib.auth import get_user_model

Manager = get_user_model() # app 증가할 경우 settins.py에 명시


# 관리자 모델 Question, Choice
class Question(models.Model):
    # 담당자 delete 되어도 설문 정보는 남아있도록 on_delete=models.SET_NULL
    writer = models.ForeignKey(Manager, null=True, on_delete=models.SET_NULL, verbose_name="작성자")
    title = models.CharField(max_length=100, verbose_name="설문지 제목")
    notice = models.TextField(blank=True, null=True, verbose_name="설문지 설명")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="최종 수정 날짜")

# Question 모델과 OneToOne 관계, 세부항목 추가 모델
class Choice(models.Model):
    CATEGORY_CHOICE = (
        ('CC', 'checkbox'),
        ('RR', 'radio'),
        ('SS', 'select'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICE, default='CC', verbose_name="유형 선택")
    choice_title = models.CharField(max_length=100, verbose_name="질문")
    item1 = models.CharField(max_length=100, verbose_name="옵션")
    item2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="옵션")
    item3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="옵션")
    item4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="옵션")
    item5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="옵션")
    item6 = models.CharField(max_length=100, blank=True, null=True, verbose_name="옵션")