from django.test import  TestCase
from core.services.freckle import Freckle
from datetime import datetime

class TestServices(TestCase):
    """docstring for TestServices"""

    def setUp(self):
        self.client = Freckle('8zh8ny1wlym4ljyi68p0je410s1aj8b', 'andela')
        self.users = self.client.get_users()
        self.projects = self.client.get_projects()
        start_date = '2014-10-27'
        end_date = '2015-02-27'
        self.entries = self.client.get_entries(self.projects, start_date, end_date)
        # self.project_times = self.client.get_project_times(self.projects, self.entries)

    def  tearDown(self):
        pass


    def test_freckle_get_users(self):

        assert 'christina@andela.co' in self.users[0]['user']['email']

    def test_freckle_get_projects(self):

        assert 'Media' in self.projects[0]['project']['name']

    def test_freckle_get_entries(self):

        assert 'pairProgrammingWithIlya' in self.entries[0]['entry']['name']

    # def test_freckle_get_project_times(self):
    #     print self.project_times
