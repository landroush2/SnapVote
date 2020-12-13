from django.contrib import admin
from django.contrib.admin import register
from .models import Survey, Question


@register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date_created', 'date_created', 'date_updated']
    search_fields = ['title', 'last_name', 'political_party']
    list_filter = ['date_created', 'date_updated']


@register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['survey','question_text', 'date_created', 'date_updated',]
    search_fields = ['title', 'last_name', 'political_party']
    list_filter = ['survey', 'date_created', 'date_updated']