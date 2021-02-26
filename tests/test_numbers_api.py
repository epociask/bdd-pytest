import pytest
import requests

from pytest_bdd import scenarios, when, then

NUMBERS_API = 'http://numbersapi.com/'

scenarios('../features/numbers_api.feature', example_converters=dict(number=str))


@pytest.fixture
@when('the Numbers API is queried with "<number>"')
def trivia_response(number):
    print("NUMBER --->", number)
    params = {'format': 'json'}
    response = requests.get(NUMBERS_API + number, params=params)
    return response


@then('the response has the number "<number>"')
def trivia_response_range(trivia_response, number):
    assert number in str(trivia_response.content)


@then('the response status code is 200')
def trivia_response_code(trivia_response):
    assert trivia_response.status_code == 200
