from django.urls import path
from canditate.api.views import api_detail_candidate_view, ApiCandidateListView, ApiVoteListView

app_name = 'candidate'

urlpatterns = [
    path('<int:id>/', api_detail_candidate_view, name="detail"),
    path('candidates', ApiCandidateListView.as_view(), name="candidates"),
    path('votes', ApiVoteListView.as_view(), name="votes"),
]
