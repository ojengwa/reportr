from django.test import TestCase
from selenium import webdriver


class TestHome(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.client.get('http://localhost:5000/login')
        assert 'Reportr' in self.browser.title()