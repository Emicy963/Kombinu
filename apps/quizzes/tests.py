from django.test import TestCase
from .models import Quiz

class QuizModelTest(TestCase):
    def setUp(self):
        self.creator = CustomUser.objects.create_user(
            username="creator@example.com",
            email="creator@example.com",
            password="creatorpass123",
            user_type="creator"
        )
        self.content = Content.objects.create(
            title="Test Content",
            description="Test description",
            creator=self.creator,
            category="tecnologia"
        )
        self.quiz = Quiz.objects.create(
            title="Test Quiz",
            content=self.content
        )

    def test_quiz_creation(self):
        """Testa se o quiz foi criado corretamente"""
        self.assertEqual(self.quiz.title, "Test Quiz")
        self.assertEqual(self.quiz.content, self.content)

    def test_content_has_quiz_after_creation(self):
        """Testa se o conteúdo reconhece que tem um quiz"""
        self.assertTrue(self.content.has_quiz)
        self.assertEqual(self.content.quiz_id, self.quiz.id)
