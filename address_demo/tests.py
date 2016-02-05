from django.test import TestCase


class TestDemoPage(TestCase):
    def test_get_demo_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

