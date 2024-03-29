from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest


# Create your tests here.

class HomePageTest(TestCase):
    ''' Toxic test for check home page '''

    def test_root_url_resolves_to_home_page_view(self):
        ''' Test: root url change to view of home_page '''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        ''' Test: home page return correct html '''
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title> Home Page </title>', html)
        self.assertTrue(html.endswith('</html>'))
