import requests
import json
import constants


def make_api_request():
    return json.loads(requests.get(constants.API_URL.format('BBAS3')).text)
