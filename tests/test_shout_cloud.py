import pytest
import requests

from pytest_bdd import scenarios, when, then

SHOUT_API = 'HTTP://API.SHOUTCLOUD.IO/V1/SHOUT'

scenarios('../features/shoutcloud_api.feature', example_converters=dict(string=str))


@pytest.fixture
@when('the shout API is queried with body: "<string>"')
def shout_response(string):
    d = '{"INPUT": "'+ string + '"}'
    print(d)
    params = {"Content-Type": "application/json"}
    response = requests.post(SHOUT_API, headers=params, data=str(d))
    return response


@then('the response has the upper cased string "<string>" as output')
def shout_response_upper_cased(shout_response, string):
    assert string.upper() == shout_response.json()["OUTPUT"]


@then('the response status code is 200')
def shout_response_code(shout_response):
    assert shout_response.status_code == 200
