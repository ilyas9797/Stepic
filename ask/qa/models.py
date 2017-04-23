from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'qa_questions'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'qa_answers'
        ordering = ['-added_at']


class QuestionManager(models.Manager):
    def new(self):
        return self.all()

    def popular(self):
        return self.ordered_by('rating')
