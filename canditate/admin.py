from django.contrib import admin
from django.contrib.admin import register
from .models import Candidate, Vote

@register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','political_party', 'votes','date_add','date_updated']
    search_fields = ['first_name', 'last_name', 'political_party']
    list_filter = ['date_add','date_updated']

@register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id','vote_title','vote_description','count_voters', 'count_canditates','start_date','end_date',]
    search_fields = ['vote_title', 'start_date', 'end_date']
    list_filter = ['candidates',]

    def has_change_permission(self, request, obj=None):
        return False

    def count_voters(self, obj):
        return str(obj.voters.all().count())

    def count_canditates(self, obj):
        return str(obj.candidates.all().count())

    count_voters.short_description = "voters"
    count_canditates.short_description = "candidates"
