import json
import requests
import datetime
from . import exceptions


class FreckleClient(object):
    """Simple client implementation to fetch json data from the v1 API."""
    def __init__(self, account_name, api_token):
        """
        Creates a ``FreckleClient`` instance.
        :account_name: Your Freckle account name.
        :api_token: Your Freckle API token.
        """
        self.account_name = account_name
        self.api_token = api_token

    def fetch_json(self, uri_path, http_method='GET', headers=None,
                   query_params=None, post_args=None):
        """
        Fetch some JSON from Letsfreckle.
        For example, fetch some entries like so:
            entries = self.fetch_json(
                'entries',
                query_params={
                    'per_page': 1000,
                    'search[from]': '2015-01-01',
                    'search[to]': '2015-01-31',
                    'search[projects]': [1423, 24545, ]),
                }
            )
        """
        # explicit values here to avoid mutable default values
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_args is None:
            post_args = {}

        # set content type and accept headers to handle JSON
        headers['Accept'] = 'application/json'
        query_params['token'] = self.api_token

        # construct the full URL without query parameters
        url = 'https://{0}.letsfreckle.com/api/{1}.json'.format(
            self.account_name, uri_path)

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request(
            http_method, url, params=query_params, headers=headers,
            data=json.dumps(post_args))

        if response.status_code != 200:
            raise exceptions.FreckleClientException(
                "Freckle API Response is not 200", response.text)

        return response.json()


class FreckleClientV2(object):
    """Simple client implementation to fetch json data from the v2 API."""
    def __init__(self, access_token):
        """
        Creates a ``FreckleClient`` instance.
        :account_name: Your Freckle account name.
        :api_token: Your Freckle API token.
        """
        self.access_token = access_token

    def fetch_json(self, uri_path, http_method='GET', headers=None,
                   query_params=None, post_args=None):
        """
        Fetch some JSON from Letsfreckle.
        For example, fetch some entries like so:
            entries = self.fetch_json(
                'entries',
                query_params={
                    'per_page': 1000,
                    'search[from]': '2015-01-01',
                    'search[to]': '2015-01-31',
                    'search[projects]': [1423, 24545, ]),
                }
            )
        """
        # explicit values here to avoid mutable default values
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_args is None:
            post_args = {}

        # set content type and accept headers to handle JSON
        headers['Accept'] = 'application/json'
        headers['User-Agent'] = "python-freckle-client/0.1",
        headers['X-FreckleToken'] = self.access_token

        # construct the full URL without query parameters
        url = 'https://api.letsfreckle.com/v2/{0}'.format(uri_path)

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request(
            http_method, url, params=query_params, headers=headers,
            data=json.dumps(post_args))

        if response.status_code != 200:
            raise exceptions.FreckleClientException(
                "Freckle API Response is not 200", response.text)

        return response.json()

class Freckle(object):

    def __init__(self, token, account=None, api_version=1):
        """Ensures that the appropraite API ebdpoint is been called."""

        if api_version == 1 and not account:
            raise AttributeError
        if api_version == 1:
            self.client = FreckleClient(account, token)
        else:
            self.client = FreckleClientV2(token)

    def get_entries(self, projects, start_date, end_date):  # pragma: no cover
        """
        Returns the entries for the given project and time frame.
        :param start_date: String representing the start date (YYYY-MM-DD).
        :param end_date: String representing the end date (YYYY-MM-DD).
        """
        entries = self.client.fetch_json(
            'entries',
            query_params={
                'per_page': 1000,
                'search[from]': start_date,
                'search[to]': end_date,
                'search[projects]': ','.join(
                    [str(project['project']['id']) for project in projects]),
            }
        )
        return entries


    def get_project_times(self, projects, entries):
        """
        Returns a dict with total time tracked per project / employee.
        The dict should look like this:
            {
                month: {
                    project_id: {
                        user_id-1: XX,
                        user_id-2: YY,
                        total: XX + YY,
                    },
                },
            }
        """
        result = {}
        projects = projects[0]
        for obj in entries:
            entry = obj['entry']
            entry_date = datetime.datetime.strptime(
                entry['date'], '%Y-%m-%d')
            if entry_date.month not in result:
                result[entry_date.month] = {}
            project_id = entry['project']['id']
            project_name = entry['project']['name']
            user_id = entry['user_id']
            print projects[0]
            # for key, project in projects:
            #     print key, project
            # if project_id not in result[entry_date.month]:
            #     result[entry_date.month][project_id] = {
            #         'total': 0, 'project_name': project_name, }
            #     if project is None:
            #         result[entry_date.month][project_id]['is_planned'] = False
            #     else:
            #         result[entry_date.month][project_id]['is_planned'] = True
            # if user_id not in result[entry_date.month][project_id]:
            #     result[entry_date.month][project_id][user_id] = 0
            # if (project and project.is_investment) or entry['billable']:
            #     minutes = entry['minutes']
            #     result[entry_date.month][project_id][user_id] += minutes
            #     result[entry_date.month][project_id]['total'] += minutes
        return result

    def get_users(self):
        """Get users from Freckle"""
        return self.client.fetch_json('users')

    def get_projects(self):
        """Get projects from Freckle"""
        return self.client.fetch_json('projects')

    def boolean_as_python(self, val):
        """Convert text to boolean"""
        if val == 'true':
            return True
        else:
            return False

    def date_as_python(self, val):
        """Convert text to date"""
        return datetime.date(*[int(x) for x in val.split("-")])

    def datetime_as_python(self, val):
        """Convert text to datetime"""
        return parse_date(val)

    def integer_as_python(self, val):
        """Convert text to integer"""
        return int(val)

    def array_as_python(self, val):
        """Convert text to list"""
        return val.split(",")

    def json_as_python(self, val):
        """Convert JSON to dict"""
        return json.load(val)