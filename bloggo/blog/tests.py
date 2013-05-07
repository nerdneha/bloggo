"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from django.test.client import Client

from models import Entry

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class BlogTest(TestCase):
    def test_list(self):
        client = Client()
        response = client.get('/entry')
        self.assertEqual(response.status_code, 200)

    def test_existing_id(self):
        client = Client()
        entry = Entry(title="Hello World!", body="Test Suite action!")
        entry.save()
        pk = entry.id
        response = client.get('/entry/' + str(pk))
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_id(self):
        client = Client()
        response = client.get('/entry/1337')
        self.assertEqual(response.status_code, 404)
