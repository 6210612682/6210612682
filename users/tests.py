from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Max
import courses

# Create your tests here.

class userViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username = 'user1' , password = '1234', email = 'user1@example.com')


    def test_view_with_authenciation(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        c.force_login(user)
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 200)


    def test_view_without_authenciation(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        response = c.get(reverse("users:index"))
        self.assertEqual(response.status_code, 302)


    def test_login_view_successful(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        response = c.post(reverse("users:login"), {'username': 'user1', 'password': '1234'})
        self.assertEqual(response.status_code, 200)


    def test_login_view_unsucessful(self):
        c = Client()
        user = User.objects.get(username = 'user1')
        response = c.post(reverse("users:login"), {'username': 'user1', 'password': '6666'})
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        c = Client()
        response = c.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)


    def test_logout_view(self):
        c = Client()
        response = c.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 200)
