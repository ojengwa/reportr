"""
Helper method to fetch data from the Trello API.
See https://trello.com/docs/index.html
"""
import json
import re

import requests
from requests_oauthlib import OAuth1


class TrelloClient(object):
    """Base class for Trello API access."""
    def __init__(self, api_key, api_secret, oauth_token, oauth_secret, rate):
        self.oauth = OAuth1(
            client_key=api_key,
            client_secret=api_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_secret)
        self.api_key = api_key
        self.api_secret = api_secret
        self.resource_owner_key = oauth_token
        self.resource_owner_secret = oauth_secret
        self.rate = rate

    def fetch_json(self, uri_path, http_method='GET', headers=None,
                   query_params=None, post_args=None):
        """Fetch some JSON from Trello."""
        # explicit values here to avoid mutable default values
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_args is None:
            post_args = {}

        # set content type and accept headers to handle JSON
        if http_method in ("POST", "PUT", "DELETE"):
            headers['Content-Type'] = 'application/json; charset=utf-8'
        headers['Accept'] = 'application/json'

        # construct the full URL without query parameters
        if uri_path[0] == '/':
            uri_path = uri_path[1:]
        url = 'https://api.trello.com/1/%s' % uri_path

        # perform the HTTP requests, if possible uses OAuth authentication
        response = requests.request(
            http_method, url, params=query_params, headers=headers,
            data=json.dumps(post_args), auth=self.oauth)

        if response.status_code != 200:
            raise Exception(
                "Trello API Response is not 200: %s" % (response.text))

        return response.json()

    def get_board(self, board_id):
        """Gets all important data for a board."""
        board = self.fetch_json(
            'boards/{0}'.format(board_id),
            query_params={
                'lists': 'open',
                'cards': 'open',
                'card_checklists': 'all',
            }
        )
        board['time_estimated_total'] = 0
        board['cost_estimated_total'] = 0
        board['time_actual_total'] = 0
        board['cost_actual_total'] = 0
        return board

    def get_cards(self, board, freckle_entries):
        """
        Returns all cards that have time trackings on Freckle.
        :param board: The trello board that should be searched for matching
          cards.
        :param freckle_entries: List of freckle entries for a given timeframe
          as returned by `FreckleClient.get_entries`.
        """
        result = []
        time_actual_total = 0
        cost_actual_total = 0
        time_free_total = 0
        cost_free_total = 0
        for card_short_id, card in freckle_entries['cards'].items():
            for tr_card in board['cards']:
                if tr_card['idShort'] == card_short_id:
                    self.enrich_card(board, None, tr_card)
                    tr_card['time_actual'] = card['minutes']
                    tr_card['cost_actual'] = card['cost']
                    time_actual_total += tr_card['time_actual']
                    cost_actual_total += tr_card['cost_actual']

                    tr_card['time_free'] = card['minutes_free']
                    tr_card['cost_free'] = card['cost_free']
                    time_free_total += tr_card['time_free']
                    cost_free_total += tr_card['cost_free']

                    for list_ in board['lists']:
                        if list_['id'] == tr_card['idList']:
                            tr_card['list_name'] = list_['name']
                    result.append(tr_card)
        board['time_actual_total'] = time_actual_total
        board['cost_actual_total'] = cost_actual_total
        board['time_free_total'] = time_free_total
        board['cost_free_total'] = cost_free_total
        return result

    def get_list(self, board, list_index):
        """
        Returns a dict with the list of the given name.
        Also attaches all cards belonging to that list to the dict.
        :param board: A board as returned by ``get_board()``
        :param list_index: Integer representing the position of the list.
          Starts at 1.
        """
        result = None
        result = board['lists'][list_index - 1]
        result['time_estimated_total'] = 0
        result['cost_estimated_total'] = 0
        list_cards = []
        for card in board['cards']:
            if card['idList'] == result['id']:
                self.enrich_card(board, result, card)
                list_cards.append(card)
        result['cards'] = list_cards
        return result

    def get_time_from_name(self, name):
        """
        Extracts the time (if given) from a name string.
        :param name: String representing the name of a checklist item.
        :returns: 0 if no time was estimated or an integer representing the
          minutes.
        """
        m = re.search(r'\((-?\d+)\)$', name)
        if not m:
            return 0
        try:
            return int(m.groups()[0])
        except TypeError:
            return 0

    def enrich_card(self, board, list_, card):
        """
        Iterates through the checklists of the card and adds estimated times.
        :param board: The board of the given card. Needed to increase the board
          total time and cost.
        :param list_: The list of the given card. Needed to increase the list
          total time and cost.
        :param card: The card to be enriched.
        """
        time_estimated = 0
        for checklist in card['checklists']:
            if checklist['name'] == 'Buffer':
                continue
            for item in checklist['checkItems']:
                minutes = self.get_time_from_name(item['name'])
                time_estimated += minutes
        card['time_estimated'] = time_estimated
        cost_estimated = time_estimated / 60.0 * self.rate
        card['cost_estimated'] = cost_estimated
        board['time_estimated_total'] += time_estimated
        board['cost_estimated_total'] += cost_estimated

        if list_ is not None:
            list_['time_estimated_total'] += time_estimated
            list_['cost_estimated_total'] += cost_estimated