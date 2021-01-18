import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\erick\Downloads\chromedriver_win32\chromedriver.exe')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    def tearDown(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)