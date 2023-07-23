from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    ''' Test new visitors '''

    def setUp(self):
        ''' Install '''
        # Chrome more faster then anather in tests
        self.browser = webdriver.Chrome()
    def tearDown(self):
        ''' Dismantling '''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_leter(self):
        ''' Test: can start list and take him later '''

        # Go to site
        self.browser.get('http://localhost:8000')

        # Watch the title of page
        self.assertIn('Home Page', self.browser.title)

        # Add the element in list

if __name__ == '__main__':
    unittest.main(warnings='ignore')