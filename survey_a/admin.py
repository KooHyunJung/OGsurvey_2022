from django.contrib import admin
from survey_a.models import Participant, Answer


# Register your models here.
# admin.site.register(Participant)
# admin.site.register(Answer)

class AnswerInline(admin.TabularInline):
    model = Answer
    min_num = 1
    verbose_name="설문 응답 항목"

@admin.register(Participant)
class ParticipantModelAdmin(admin.ModelAdmin): 
    list_display = ('id','question_id', 'phone')
    search_fields = ('question_id', 'phone')
    search_help_text = '[설문지 질문 항목, 전화번호] 항목으로 검색 가능합니다'
    inlines = [AnswerInline]