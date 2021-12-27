# Rozważmy stronę https://randomuser.me/, która posiada API do tworzenia pseudolosowej osoby.
# Przestudiuj to API pod kątem otrzymywanego pola JSON,  a następnie napisz klasę testującą,
# która będzie przetwarzała otrzymane dane w postaci JSON (nie korzystając z atrap - normalnie testujemy).
# Następnie napisz kolejną klasę, przepisując wyżej napisane testy na atrapy
# (tutaj zakładamy, że nie mamy dostępu do danych z API, ale wiemy jakie dane powinny przyjść).
import unittest

import requests
import json
from assertpy import assert_that
from unittest.mock import *


class Person:
    def __init__(self):
        response_API = requests.get('https://randomuser.me/api/?format=json')
        self.p = json.loads(response_API.text)


class JsonTest (unittest.TestCase):
    def setUp(self):
        self.per = Person()
        self.j = self.per.p

    def test_gender(self):
        assert_that({self.j['results'][0]['gender']}).is_subset_of({'female', 'male'})

    def test_name(self):
        assert_that(self.j['results'][0]['name']).contains_key('title', 'first', 'last')

    def test_location(self):
        assert_that(self.j['results'][0]['location']).contains_key('street', 'city', 'state', 'country', 'postcode', 'coordinates', 'timezone')

    def test_email(self):
        assert_that(self.j['results'][0]['email']).matches(r'\w+@\w+\.\w+')

    def test_login(self):
        assert_that(self.j['results'][0]['login']).contains_key('uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256')

    def test_dob(self):
        assert_that(self.j['results'][0]['dob']).contains_key('date', 'age')

    def test_registered(self):
        assert_that(self.j['results'][0]['registered']).contains_key('date', 'age')

    def test_phone(self):
        assert_that(self.j['results'][0]['phone']).is_subset_of('0123456789()- ')

    def test_cell(self):
        assert_that(self.j['results'][0]['cell']).is_subset_of('0123456789()- ')

    def test_id(self):
        assert_that(self.j['results'][0]['id']).contains_key('name', 'value')

    def test_picture(self):
        assert_that(self.j['results'][0]['picture']).contains_key('large', 'medium', 'thumbnail')

    def test_nat(self):
        assert_that(self.j['results'][0]['nat']).matches(r'[A-Z]{2}')
        print(self.j)

    def tearDown(self):
        self.j = None


class Mock_res:
    def __init__(self, a):
        self.text = a


class MockPerson(unittest.TestCase):
    def setUp(self):
        def sideEffect(arg1):
            n = {'results': [{'gender': 'male', 'name': {'title': 'Monsieur', 'first': 'Samir', 'last': 'Renaud'}, 'location': {'street': {'number': 4964, 'name': 'Cours Charlemagne'}, 'city': 'Altnau', 'state': 'Jura', 'country': 'Switzerland', 'postcode': 7202, 'coordinates': {'latitude': '-53.2844', 'longitude': '-147.7335'}, 'timezone': {'offset': '+9:00', 'description': 'Tokyo, Seoul, Osaka, Sapporo, Yakutsk'}}, 'email': 'samir.renaud@example.com', 'login': {'uuid': 'dde72060-6ef5-4e52-af1a-2d60b3115b82', 'username': 'bigostrich251', 'password': 'warlord', 'salt': 'A50x5vkx', 'md5': 'd3fb8b4af265307f8dfbf4b373bd3223', 'sha1': '504e3e87a87b1ec4d49017d9620e9e460484f0d3', 'sha256': '87c9dd0d25f67e49ca104d2637d531742386f6c5a4b5e4359a776a2aa7e773e3'}, 'dob': {'date': '1990-12-06T05:01:32.291Z', 'age': 31}, 'registered': {'date': '2009-03-28T00:09:07.335Z', 'age': 12}, 'phone': '076 103 75 11', 'cell': '076 146 76 22', 'id': {'name': 'AVS', 'value': '756.8337.7460.83'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/2.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/2.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/2.jpg'}, 'nat': 'CH'}], 'info': {'seed': 'cb863c60e6735fd8', 'results': 1, 'page': 1, 'version': '1.3'}}
            return Mock_res(json.dumps(n))
        # prepare mock get
        requests.get = Mock(name='get')
        requests.get.side_effect = sideEffect

        response_API = requests.get('https://example.com')
        self.j = json.loads(response_API.text)

    def test_gender2(self):
        assert_that({self.j['results'][0]['gender']}).is_subset_of({'female', 'male'})

    def test_name2(self):
        assert_that(self.j['results'][0]['name']).contains_key('title', 'first', 'last')

    def test_location2(self):
        assert_that(self.j['results'][0]['location']).contains_key('street', 'city', 'state', 'country', 'postcode', 'coordinates', 'timezone')

    def test_email2(self):
        assert_that(self.j['results'][0]['email']).matches(r'\w+@\w+\.\w+')

    def test_login2(self):
        assert_that(self.j['results'][0]['login']).contains_key('uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256')

    def test_dob2(self):
        assert_that(self.j['results'][0]['dob']).contains_key('date', 'age')

    def test_registered2(self):
        assert_that(self.j['results'][0]['registered']).contains_key('date', 'age')

    def test_phone2(self):
        assert_that(self.j['results'][0]['phone']).is_subset_of('0123456789()- ')

    def test_cell2(self):
        assert_that(self.j['results'][0]['cell']).is_subset_of('0123456789()- ')

    def test_id2(self):
        assert_that(self.j['results'][0]['id']).contains_key('name', 'value')

    def test_picture2(self):
        assert_that(self.j['results'][0]['picture']).contains_key('large', 'medium', 'thumbnail')

    def test_nat2(self):
        assert_that(self.j['results'][0]['nat']).matches(r'[A-Z]{2}')

    def tearDown(self):
        self.j = None


if __name__ == '__main__':
    unittest.main()