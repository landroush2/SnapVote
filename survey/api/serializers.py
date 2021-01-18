from rest_framework import serializers
from survey.models import *

class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = "__all__"


class QuestionSerialier(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerialier(serializers.ModelSerializer):

    question = QuestionSerialier()

    class Meta:
        model = Answer
        fields = ['survey','elector','question','question','answer','date_created']


class SubmissionSerialier(serializers.ModelSerializer):

    answers = AnswerSerialier(many=True)

    class Meta:
        model = Submission
        fields = ['elector','survey','answers','date_created']