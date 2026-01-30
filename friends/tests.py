from django.test import TestCase
from django.contrib.auth import get_user_model
from friends.models import Follow

User = get_user_model()

class FriendsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_follow_user(self):
        Follow.objects.create(follower=self.user1, following=self.user2)
        self.assertTrue(Follow.objects.filter(follower=self.user1, following=self.user2).exists())
        self.assertEqual(self.user1.following.count(), 1)
        self.assertEqual(self.user2.followers.count(), 1)

    def test_unfollow_user(self):
        follow = Follow.objects.create(follower=self.user1, following=self.user2)
        follow.delete()
        self.assertFalse(Follow.objects.filter(follower=self.user1, following=self.user2).exists())
