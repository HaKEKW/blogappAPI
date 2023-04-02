from django.test import TestCase
from django.contrib.auth import get_user_model

from posts.models import Post


class BlogTests(TestCase):
    user = None

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='user1',
            email='user1@email.com',
            password='strongpass',
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='Test title',
            body='Test body',
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'user1')
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(str(self.post), 'Test title')

