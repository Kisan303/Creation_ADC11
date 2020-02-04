from django.test import TestCase
from django.urls import reverse
from account.models import Org, ChildEduDonor, User, Receiver, Upload
import json
import unittest

class OrgTestCase(self):
	def setUp(self):
		Org.objects.create(org_name="nhhs", email="nhhs@gmail.com", password="lilili12", address="ktm", contact=986712345, total_amt=4000, bank_acc=34566)
		
	def test_org_test(self):
		nhhs=Org.objects.get(name="nhhs")
		self.assertEqual(nhhs.name(), 'Nepal helping hands society')