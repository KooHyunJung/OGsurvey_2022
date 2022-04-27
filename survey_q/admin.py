from django.contrib import admin
from survey_q.models import Question, Choice


# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 3
    max_num = 6
    verbose_name="설문 질문 항목"

@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin): 
    list_display = ('id','writer','title')
    search_fields = ('title', 'writer__username')
    search_help_text = '[설문지 제목, 작성자 이름] 항목으로 검색 가능합니다'
    inlines = [ChoiceInline]