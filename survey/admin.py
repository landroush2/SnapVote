from django.contrib import admin
from django.contrib.admin import register
from .models import *


class QuestionInline(admin.TabularInline):
    model = Question

    def has_add_permission(self, request, obj):
        return False


@register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date_created', 'date_updated']
    search_fields = ['title', 'last_name', 'political_party']
    list_filter = ['date_created', 'date_updated']
    inlines = [
        QuestionInline,
    ]


@register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['survey','question_text', 'choices', 'date_created', 'date_updated',]
    search_fields = ['title', 'last_name', 'political_party']
    list_filter = ['survey', 'date_created', 'date_updated']


@register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question','answer', 'date_created',]
    search_fields = ['answer',]
    list_filter = ['survey', 'elector','date_created']


@register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['survey','elector', 'date_created']
    search_fields = ['survey',]
    list_filter = ['survey', 'date_created', 'elector']
