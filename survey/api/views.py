from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
import json
# import models
from elector.models import Elector
from survey.models import Survey, Question, Answer, Submission
from survey.api.serializers import SurveySerializer, QuestionSerialier, AnswerSerialier, SubmissionSerialier


class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = []

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SurveySerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialier
    permission_classes = []
    lookup_field = ['survey',]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = QuestionSerialier(queryset, many=True)
        return Response(serializer.data)


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerialier
    permission_classes = []

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = AnswerSerialier(queryset, many=True)
        return Response(serializer.data)


class SubmissionList(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerialier
    permission_classes = []

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = SubmissionSerialier(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def get_survey_for_elector(request,electorId):
    try:
        elector = Elector.objects.get(elector_id=electorId)
        surveys = []
        all_survey = Survey.objects.all()
        submissions = Submission.objects.filter(elector=elector.id)
        for survey in all_survey:
            submit = False
            for sub in submissions:
                if survey.id == sub.survey.id:
                    submit = True
            if not submit:
                surveys.append(survey)
    except Survey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  SurveySerializer(surveys, many=True)
        return Response(serializer.data)



@api_view(['GET', ])
def question_view_by_survey(request,survey):
    try:
        questions = Question.objects.filter(survey=survey)
    except Survey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  QuestionSerialier(questions, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def answers_by_survey_and_elector(request,survey,elector):
    try:
        answers = Answer.objects.filter(survey=survey,elector=elector)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  AnswerSerialier(answers, many=True)
        return Response(serializer.data)


@api_view(['POST', ])
def submit_survey(request,survey,electorId):

    if request.method == 'POST':
        try:
            # get the survey object
            survey = Survey.objects.get(id=int(survey))
            # get elector
            elector = Elector.objects.get(elector_id=electorId)
            # get answers given by the user
            data = json.loads(request.body.decode('utf-8'))
            # create answers from data

            print(data)
            answers = []
            for answer in data:
                question = Question.objects.get(id=int(answer['questionId']))
                if isinstance(answer['value'],str):
                    answer_text = answer['value']
                    new_answer = Answer.objects.create(survey=survey,elector=elector,question=question,answer=answer_text)
                    answers.append(new_answer)
                else:
                    answer_text = answer['value']['value']
                    new_answer = Answer.objects.create(survey=survey, elector=elector, question=question,
                                                       answer=answer_text)
                    answers.append(new_answer)
            # create submission object
            submission = Submission(survey=survey, elector=elector)
            submission.save()
            # add answers to my submission and save it
            for answer in answers:
                submission.answers.add(answer)
            submission.save()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': "Thanks for your feedback on this survey."},status=status.HTTP_201_CREATED)
