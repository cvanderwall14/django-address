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


class CityModelTest(TestCase):
    def setUp(self):
        self.city = City.objects.create(name='San Francisco')

    def test_string_representation(self):
        txt = str(self.city)
        self.assertEqual(txt, 'San Francisco')


class PostalCodeModelTest(TestCase):
    def setUp(self):
        self.postal_code = PostalCode.objects.create(value='94123')

    def test_string_representation(self):
        txt = str(self.postal_code)
        self.assertEqual(txt, '94123')
