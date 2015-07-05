from django.db import models

# Create your models here.


class Question(models.Model):
    question_sms=models.CharField(max_length=200)
    date_pu=models.DateTimeField('date creation')
    def __str__(self):
        return self.question_sms


class Reponse(models.Model):
    question=models.ForeignKey(Question)
    reponse_sms=models.CharField(max_length=160)
    def __str__(self):
        return self.reponse_sms
