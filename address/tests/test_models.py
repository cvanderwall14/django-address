from django.test import TestCase

from address.models import *


class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='United States')

    def test_string_representation(self):
        txt = str(self.country)
        self.assertEqual(txt, 'United States')

