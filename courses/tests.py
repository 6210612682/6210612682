from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.hashers import make_password
from .models import Course
from users.views import *
# Create your tests here.


class coursesViewsTestCase(TestCase):


    def setUp(self):

        course = Course.objects.create(c_id = 'CN331' ,c_name ='Software Engineering' ,semestry = '1' ,year = 2564 ,vacancy = 3, status = 'OPEN')

        password = make_password('1234')
        user = User.objects.create(username='user1', password=password, email='user1@example.com', is_superuser=True)
        user.save()
        course.students.add(user)


    def test_views_index(self):
        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code,200)


    def test_views_show_course_page(self):
        c = Client()
        x = Course.objects.first()
        response = c.get(reverse('courses:course', args=(x.c_id,)))
        self.assertEqual(response.status_code,200)


    def test_views_show_admin_page(self):
        c = Client()
        x = Course.objects.first()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('courses:course', args=(x.c_id,)))
        self.assertEqual(response.status_code,200)


    def test_cannot_apply_course(self):
        c = Client()
        user = User.objects.create(username = 'user2' , password = '1234' , email = 'user2@example.com')
        x = Course.objects.first()
        response = c.get(reverse('courses:book' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(),1)


    def test_can_apply_course(self):
        c = Client()
        user = User.objects.create(username = 'user2' , password = '1234' , email = 'user2@example.com')
        x = Course.objects.first()
        x.vancancy = 2
        x.save()
        c.force_login(user)
        response = c.get(reverse('courses:book' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(),2)


    def test_cannot_apply_full_course(self):
        c = Client()
        user = User.objects.create(username = 'user3', password = '1234', email = 'user3@gmail.com')
        x = Course.objects.first()
        x.vacancy = 1
        x.save()
        c.force_login(user)
        response = c.get(reverse('courses:book' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(), 1)


    def test_cannot_cancel_course(self):
        c = Client()
        user = User.objects.create(username = 'user2' , password = '1234' , email = 'user2@example.com')
        x = Course.objects.first()
        response = c.get(reverse('courses:cancel' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(),1)


    def test_can_cancel_course(self):
        c = Client()
        user = User.objects.create(username = 'user2' , password = '1234' , email = 'user2@example.com')
        x = Course.objects.first()
        x.students.add(user)
        c.force_login(user)
        response = c.get(reverse('courses:cancel' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(),1)


    def test_cannot_cancel_enroll_course(self):
        c = Client()
        user = User.objects.create(username = 'user3', password = '1234', email = 'user3@gmail.com')
        x = Course.objects.first()
        c.force_login(user)
        response = c.get(reverse('courses:cancel' ,args=(x.c_id,)))
        self.assertEqual(x.students.count(), 1)
