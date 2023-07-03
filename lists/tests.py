from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    ''' Toxic test for check if works test '''

    def test_bad_maths(self):
        ''' Test: Wrong maths result '''
        self.assertEquals(1 + 1, 3)