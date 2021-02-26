import pytest
import requests

from pytest_bdd import scenarios, when, then

BEER_API = 'https://api.punkapi.com/v2/beers/'

scenarios('../features/beers_api.feature', example_converters=dict(beer=str, beer_ph=float))


@pytest.fixture
@when('the Beer API is queried with body: "<beer_id>"')
def beer_response(beer_id):
    params = {'format': 'json'}
    response = requests.get(BEER_API + "/" + beer_id, headers=params)
    return response


@then('the response shows PH content of "<beer_ph>"')
def beer_response_upper_cased(beer_response, beer_ph):
    assert float(beer_response.json()[0]["ph"]) == beer_ph


@then('the response status code is 200')
def beer_response_code(beer_response):
    assert beer_response.status_code == 200
