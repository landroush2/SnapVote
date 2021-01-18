from django.db import models
from elector.models import Elector


class Survey(models.Model):
    title = models.CharField(max_length=25,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):

    TextInput = 'TextInput'
    NumericInput = 'NumericInput'
    SelectionGroup = 'SelectionGroup'
    MultipleSelectionGroup = 'MultipleSelectionGroup'
    QUESTION_TYPE = [
        (TextInput, 'TextInput'),
        (NumericInput, 'NumericInput'),
        (SelectionGroup, 'SelectionGroup'),
        (MultipleSelectionGroup, 'MultipleSelectionGroup'),
    ]

    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,null=True,blank=True)
    question_text = models.TextField(null=True,blank=True)
    question_type = models.CharField(max_length=255,choices=QUESTION_TYPE,default=TextInput)
    choices = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True, blank=True)
    elector = models.ForeignKey(Elector,on_delete=models.CASCADE,null=True,blank=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Survey {}: , Answer: {}".format(self.question, self.answer)

class Submission(models.Model):
    elector = models.ForeignKey(Elector,on_delete=models.CASCADE,null=True,blank=True)
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,null=True,blank=True)
    answers = models.ManyToManyField(Answer)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):

        return "Submission of {} by {}".format(self.survey,self.elector.first_name)