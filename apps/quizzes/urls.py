from django.urls import path
from .views import QuizDetailView, QuizGenerationView, QuizSubmissionView, QuizManualCreationView


urlpatterns = [
    path("<uuid:id>/", QuizDetailView.as_view(), name="quiz-detail"),
    path("<uuid:quiz_id>/submit/", QuizSubmissionView.as_view(), name="quiz-submit"),
    path(
        "contents/<uuid:content_id>/generate-quiz/",
        QuizGenerationView.as_view(),
        name="quiz-generate",
    ),
    path(
        "contents/<uuid:content_id>/manual-quiz/",
        QuizManualCreationView.as_view(),
        name="quiz-manual-create",
    ),
]
