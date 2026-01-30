from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
    def test_profile_creation(self):
        # Profile should be created by signal
        self.assertTrue(Profile.objects.filter(user=self.user).exists())
        
    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302) # Should redirect
        self.assertRedirects(response, reverse('home'))

    def test_post_creation(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('home'), {
            'content': 'This is a test post'
        })
        self.assertEqual(response.status_code, 302) # Redirect to home
        self.assertTrue(Post.objects.filter(content='This is a test post').exists())

    def test_comment_creation(self):
        self.client.login(username='testuser', password='password123')
        post = Post.objects.create(author=self.user, content='Test Post')
        
        response = self.client.post(reverse('post_detail', args=[post.id]), {
            'content': 'Nice post!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(content='Nice post!', post=post).exists())

    def test_like_post(self):
        self.client.login(username='testuser', password='password123')
        post = Post.objects.create(author=self.user, content='Like me')
        
        response = self.client.get(reverse('like_post', args=[post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Like.objects.filter(user=self.user, post=post).exists())

    def test_follow_user(self):
        other_user = User.objects.create_user(username='other', password='password123')
        self.client.login(username='testuser', password='password123')
        
        response = self.client.get(reverse('follow_user', args=[other_user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Follow.objects.filter(follower=self.user, following=other_user).exists())
