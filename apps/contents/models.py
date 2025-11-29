from django.db import models
from apps.accounts.models import CustomUser
import uuid


class Content(models.Model):
    CATEGORY_CHOICES = (
        ("tecnologia", "Tecnologia"),
        ("negocios", "Negócios"),
        ("design", "Design"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="created_contents"
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def has_quiz(self):
        return hasattr(self, "quiz")

    @property
    def quiz_id(self):
        if self.has_quiz:
            return self.quiz.id
        return None
