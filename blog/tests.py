from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post',
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, self.user)

    def test_post_string_representation(self):
        self.assertEqual(str(self.post), 'Test Post')
