from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class PostsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.client.login(username='u', password='p')

    def test_create_post(self):
        url = reverse('post-list')
        resp = self.client.post(url, {'title': 'T', 'content': 'C'}, format='json')
        self.assertEqual(resp.status_code, 201)



