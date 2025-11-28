from django.test import TestCase
from apps.accounts.models import CustomUser
from apps.contents.models import Content


class ContentModelTest(TestCase):
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

    def test_content_creation(self):
        """Testa se o conteúdo foi criado corretamente"""
        self.assertEqual(self.content.title, "Test Content")
        self.assertEqual(self.content.category, "tecnologia")
        self.assertEqual(self.content.creator, self.creator)

    def test_has_quiz_property(self):
        """Testa a propriedade has_quiz quando não há quiz"""
        self.assertFalse(self.content.has_quiz)

    def test_quiz_id_property_without_quiz(self):
        """Testa a propriedade quiz_id quando não há quiz"""
        self.assertIsNone(self.content.quiz_id)

    def test_content_str_representation(self):
        """Testa a representação string do conteúdo"""
        self.assertEqual(str(self.content), "Test Content")

    def test_content_categories(self):
        """Testa as categorias disponíveis"""
        categories = ["tecnologia", "negocios", "design"]
        for category in categories:
            content = Content.objects.create(
                title=f"Content {category}",
                description="Test description",
                creator=self.creator,
                category=category
            )
            self.assertEqual(content.category, category)

    def test_content_belongs_to_creator(self):
        """Testa que o conteúdo pertence ao criador"""
        self.assertIn(self.content, self.creator.created_contents.all())
