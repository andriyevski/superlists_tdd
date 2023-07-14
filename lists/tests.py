from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):
    ''' Toxic test for check home page '''

    def test_root_url_resolves_to_home_page_view(self):
        ''' Test: root url change to view of home_page '''
        found = resolve('/')
        self.assertEqual(found.func, home_page)