from django.db import models
from elector.models import Elector


class Survey(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,null=True,blank=True)
    question_text = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.survey.title


class Answers(models.Model):
    survey = models.ForeignKey(Survey,on_delete=models.CASCADE,null=True,blank=True)
    elector = models.ForeignKey(Elector,on_delete=models.CASCADE,null=True,blank=True)


