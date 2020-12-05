from django.contrib import admin
from django.contrib.admin import register
from .models import Elector

@register(Elector)
class ElectorAdmin(admin.ModelAdmin):
    list_display = ['elector_id', 'first_name', 'last_name', 'sexe', 'date_of_issuance', 'date_of_expire']
    search_fields = ['elector_id', 'first_name', 'last_name', 'political_party']
    list_filter = ['date_of_issuance', 'date_of_expire', 'sexe']