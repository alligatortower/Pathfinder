"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class pages_work(TestCase):
	def setUp(self):
		self.client = Client()
	def test_200(self):
		"""Tests that pages return a 200"""
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
