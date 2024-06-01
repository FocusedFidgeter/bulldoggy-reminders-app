"""
This module contains API tests for the Bulldoggy app.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

from playwright.sync_api import APIRequestContext
from testlib.inputs import User


# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_successful_api_login(bulldoggy_api: APIRequestContext, user: User, base_url: str):
  """
  Test case for a successful API login.

  This function tests the functionality of the API login endpoint by sending a POST request to the '/login' route with valid user credentials. It asserts that the response is successful (status code 200) and that the redirected URL matches the expected value. It also checks that the 'reminders_session' cookie is set correctly.

  Parameters:
  - bulldoggy_api (APIRequestContext): The API request context object used to send the login request.
  - user (User): The User object representing the user credentials.
  - base_url (str): The base URL of the API.

  Returns:
  None
  """

  response = bulldoggy_api.post('/login', form={'username': user.username, 'password': user.password})
  assert response.ok
  assert response.url == f'{base_url}/reminders'

  cookie = bulldoggy_api.storage_state()['cookies'][0]
  assert cookie['name'] == 'reminders_session'
  assert cookie['value']
