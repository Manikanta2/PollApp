from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
