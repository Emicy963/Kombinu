from django.db import models
from apps.contents.models import Content

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    content = models.OneToOneField(Content, on_delete=models.CASCADE, related_name="quiz")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_test = models.TextField()

    def __str__(self):
        return self.question_test[:50]
