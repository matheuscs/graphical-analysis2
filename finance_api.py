import requests
import constants


def make_api_request():
    return requests.get(constants.API_URL.format('BBAS3')).text
