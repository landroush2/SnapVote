from django.urls import path
from elector.api.views import api_detail_elector_view, api_elector_vote_view

app_name = 'elector'

urlpatterns = [
    path('<str:id>/', api_detail_elector_view, name="info"),
    path('vote/<str:id>/', api_elector_vote_view, name="vote"),
]
