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

class QuestionAndOptionModelTest(TestCase):
    def setUp(self):
        creator = CustomUser.objects.create_user(
            username="creator@example.com",
            email="creator@example.com",
            password="creatorpass123",
            user_type="creator"
        )
        content = Content.objects.create(
            title="Test Content",
            description="Test description",
            creator=creator,
            category="tecnologia"
        )
        self.quiz = Quiz.objects.create(title="Test Quiz", content=content)
        self.question = Question.objects.create(
            quiz=self.quiz,
            question_text="What is 2+2?"
        )
        self.correct_option = Option.objects.create(
            question=self.question,
            text="4",
            is_correct=True
        )
        self.wrong_option = Option.objects.create(
            question=self.question,
            text="5",
            is_correct=False
        )

    def test_question_creation(self):
        """Testa se a questão foi criada corretamente"""
        self.assertEqual(self.question.question_text, "What is 2+2?")
        self.assertEqual(self.question.quiz, self.quiz)

    def test_options_creation(self):
        """Testa se as opções foram criadas corretamente"""
        self.assertTrue(self.correct_option.is_correct)
        self.assertFalse(self.wrong_option.is_correct)

    def test_question_has_multiple_options(self):
        """Testa se a questão tem múltiplas opções"""
        self.assertEqual(self.question.options.count(), 2)


class QuizSubmissionModelTest(TestCase):
    def setUp(self):
        self.learner = CustomUser.objects.create_user(
            username="learner@example.com",
            email="learner@example.com",
            password="learnerpass123",
            user_type="learner"
        )
        creator = CustomUser.objects.create_user(
            username="creator@example.com",
            email="creator@example.com",
            password="creatorpass123",
            user_type="creator"
        )
        content = Content.objects.create(
            title="Test Content",
            description="Test description",
            creator=creator,
            category="tecnologia"
        )
        self.quiz = Quiz.objects.create(title="Test Quiz", content=content)
        self.submission = QuizSubmission.objects.create(
            user=self.learner,
            quiz=self.quiz,
            score=8
        )

    def test_submission_creation(self):
        """Testa se a submissão foi criada corretamente"""
        self.assertEqual(self.submission.user, self.learner)
        self.assertEqual(self.submission.quiz, self.quiz)
        self.assertEqual(self.submission.score, 8)

    def test_unique_submission_constraint(self):
        """Testa se não é possível criar submissões duplicadas"""
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            QuizSubmission.objects.create(
                user=self.learner,
                quiz=self.quiz,
                score=5
            )
