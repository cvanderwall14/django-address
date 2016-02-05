from django.test import TestCase

from address.models import *


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='United States')

    def test_string_representation(self):
        txt = str(self.country)
        self.assertEqual(txt, 'United States')


class StateModelTest(TestCase):
    def setUp(self):
        self.state = State.objects.create(name='California')

    def test_string_representation(self):
        txt = str(self.state)
        self.assertEqual(txt, 'California')
