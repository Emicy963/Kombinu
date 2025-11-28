from django.test import TestCase
from apps.accounts.models import CustomUser


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="test@example.com",
            email="test@example.com",
            password="testpass123",
            user_type="learner"
        )

    def test_user_creation(self):
        """Testa se o usuário foi criado corretamente"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.user_type, "learner")
        self.assertTrue(self.user.check_password("testpass123"))

    def test_user_str_representation(self):
        """Testa a representação string do usuário"""
        self.assertEqual(str(self.user), "test@example.com")

    def test_email_is_unique(self):
        """Testa que o email deve ser único"""
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(
                username="test2@example.com",
                email="test@example.com",  # Email duplicado
                password="testpass456",
                user_type="creator"
            )

    def test_user_type_choices(self):
        """Testa os tipos de usuário disponíveis"""
        creator = CustomUser.objects.create_user(
            username="creator@example.com",
            email="creator@example.com",
            password="creatorpass123",
            user_type="creator"
        )
        self.assertEqual(creator.user_type, "creator")
        
        learner = CustomUser.objects.create_user(
            username="learner@example.com",
            email="learner@example.com",
            password="learnerpass123",
            user_type="learner"
        )
        self.assertEqual(learner.user_type, "learner")
