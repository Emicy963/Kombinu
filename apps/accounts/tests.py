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