from django.urls import path
from survey.api.views import SurveyList, QuestionList, question_view_by_survey,\
AnswerList, answers_by_survey_and_elector, SubmissionList, submit_survey, get_survey_for_elector

app_name = 'survey'

urlpatterns = [
    path('survey_list/', SurveyList.as_view(), name="surveys"),
    path('question_list/', QuestionList.as_view(), name="questions"),
    path('answer_list/', AnswerList.as_view(), name="answers"),
    path('submission_list/', SubmissionList.as_view(), name="submission"),
    path('get_survey_for_elector/<str:electorId>/', get_survey_for_elector, name="get_survey_for_elector"),
    path('answer/<int:survey>/<int:elector>/', answers_by_survey_and_elector, name="answers_by_elector_and_survey"),
    path('question_list/<int:survey>/', question_view_by_survey, name="questions_by_survey"),
    path('submit_survey/<int:survey>/<str:electorId>/', submit_survey, name="submit_survey"),
]
