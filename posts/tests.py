from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post, Comment, Like

User = get_user_model()

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_post(self):
        post = Post.objects.create(author=self.user, content='Hello World')
        self.assertEqual(post.content, 'Hello World')
        self.assertEqual(post.author, self.user)

    def test_comment_on_post(self):
        post = Post.objects.create(author=self.user, content='Post to comment')
        comment = Comment.objects.create(post=post, author=self.user, content='Nice post')
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.content, 'Nice post')

    def test_like_post(self):
        post = Post.objects.create(author=self.user, content='Post to like')
        Like.objects.create(user=self.user, post=post)
        self.assertEqual(post.likes.count(), 1)
