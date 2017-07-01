from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=300)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
