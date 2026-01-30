from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post, Like
from notifications.models import Notification

User = get_user_model()

class NotificationTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.post = Post.objects.create(author=self.user1, content='Test post')

    def test_like_notification(self):
        # User2 likes User1's post
        Like.objects.create(user=self.user2, post=self.post)
        
        # Check if notification was created for User1
        notification = Notification.objects.filter(recipient=self.user1, sender=self.user2).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.notification_type, 'like')
