from django.test import TestCase
from django.urls import reverse

from. import views
from main.models register
from datetime import datetime

class HeraldTesting(TestCase):
	def setUp(self):
		register.objects.create(first_name="Python", last_name="best", username="tulsi", contact=12333, address="ktm", age=32, email="bb@gmail.com", password="tytyt", confirm_password="tytyt")

	def test_ORM(self):
		reg=register.objects.get(first_name="Python")
		self.assertEqual(reg.first_name, 'Python')

