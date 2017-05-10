from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('qa:question-detail', args=(self.id,))

    def get_creation_time(self):
        return self.added_at

    class Meta:
        db_table = 'qa_questions'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'qa_answers'
        ordering = ['-added_at']

