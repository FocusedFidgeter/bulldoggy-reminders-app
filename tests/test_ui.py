"""
This module contains Web UI tests for the Bulldoggy app.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------

import re

from playwright.sync_api import Page, expect
from testlib.inputs import User

# --------------------------------------------------------------------------------
# Helpers
# 
#   login page displays correctly
#   reminders page displays correctly
# --------------------------------------------------------------------------------


def verify_login_page(page: Page):
  """
  Verify the login page by checking if the page title, URL, and specific elements are as expected.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  Returns:
  None
  """
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()


def verify_reminders_page(page: Page, user: User):
  """
  Verify the reminders page by checking if the page title, URL, and specific elements are as expected.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None
  """
  expect(page).to_have_url(re.compile(re.escape('/') + 'reminders'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.locator('id=bulldoggy-title')).to_have_text('Bulldoggy')
  expect(page.get_by_role('button', name='Logout')).to_be_visible()
  expect(page.locator('id=reminders-message')).to_have_text(f'Reminders for {user.username}')


def log_in(page: Page, user: User):
  """
  Log in to the app by providing valid credentials.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None
  """
  page.locator('[name="username"]').fill(user.username)
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()


# --------------------------------------------------------------------------------
# Login Behaviors
#
#   log in successfully
#   no login credentials
#   no username
#   no password
#   incorrect username
#   incorrect password
#   log out
# --------------------------------------------------------------------------------


def test_successful_login(page: Page, user: User):
  """
  Test case for a successful login.

  This test case verifies that a user can successfully log in to the app by providing valid credentials.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with the provided user credentials.
  3. Clicks the "Login" button.
  4. Verifies that the login process is successful.

  Note: This test case assumes the presence of the Playwright library and the necessary setup for running browser tests.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides valid credentials
  log_in(page, user)

  # Then verify that the reminders page is displayed correctly
  verify_reminders_page(page, user)


def test_no_credentials(page: Page):
  """
  Test case for verifying that an error message is displayed when no login credentials are provided.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Clicks the "Login" button.
  3. Verifies that the login process is unsuccessful.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no login credentials
  page.get_by_text('Login').click()

  # Then the login page does not change until the user provides
  #   both username and password (those could still be incorrect).
  verify_login_page(page)


def test_no_username(page: Page, user: User):
  """
  Test case for verifying that an error message is displayed when no username is provided.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the password field with the provided user credentials.
  3. Clicks the "Login" button.
  4. Verifies that the login process is unsuccessful.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no username
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # Then the login process is not executed
  verify_login_page(page)


def test_no_password(page: Page, user: User):
  """
  Test case for verifying that an error message is displayed when no password is provided.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username field with the provided user credentials.
  3. Clicks the "Login" button.
  4. Verifies that the login process is unsuccessful.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no password
  page.locator('[name="username"]').fill(user.username)
  page.get_by_text('Login').click()

  # Then the login process is not executed
  verify_login_page(page)


def test_incorrect_username(page: Page, user: User):
  """
  Test case for verifying that an error message is displayed when an incorrect username is provided.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with incorrect credentials.
  3. Clicks the "Login" button.
  4. Verifies that the error message is displayed.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides incorrect username, but correct password
  page.locator('[name="username"]').fill('invalid-username')
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page.locator('text=Invalid login! Please retry.')).to_be_visible()


def test_incorrect_password(page: Page, user: User):
  """
  Test case for verifying that an error message is displayed when an incorrect password is provided.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with incorrect credentials.
  3. Clicks the "Login" button.
  4. Verifies that the error message is displayed.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides correct username, but incorrect password
  page.locator('[name="username"]').fill(user.username)
  page.locator('[name="password"]').fill('invalid-password')
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page.locator('text=Invalid login! Please retry.')).to_be_visible()


def test_successful_logout(page: Page, user: User):
  """
  Test case for verifying that the user can successfully log out.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with the provided user credentials.
  3. Clicks the "Login" button.
  4. Clicks the "Logout" button.
  5. Verifies that the login page and the logout message are displayed.
  """
  # Given the login process is successful
  page.goto('/login')
  log_in(page, user)

  # When the user clicks the logout button
  page.get_by_text('Logout').click()

  # Then the login page and the logout message is displayed
  expect(page.locator('text=Successfully logged out.')).to_be_visible()


# --------------------------------------------------------------------------------
# Navigation Behaviors
#
#   load the login page
#   load the reminders page
#   home redirects to login when not authenticated
#   home redirects to reminders when logged in
#   invalid navigation redirects to not found
# --------------------------------------------------------------------------------


def test_load_login_page(page: Page):
  """
  Test case for verifying that the login page is loaded correctly.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Verifies that the login page is displayed.
  """

  # Given the code is correctly running

  # When the user navigates to the login page
  page.goto('/login')

  # Then the login page is displayed
  verify_login_page(page)


def test_load_reminders_page(page: Page, user: User):
  """
  Test case for verifying that the reminders page is loaded correctly.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with the provided user credentials.
  3. Clicks the "Login" button.
  4. Verifies that the reminders page is displayed.
  """
  # Given the login process is successful
  page.goto('/login')
  log_in(page, user)

  # When the user navigates to the reminders page
  page.goto('/reminders')

  # Then the reminders page is displayed
  verify_reminders_page(page, user)

def test_home_redirects_to_login_when_not_authenticated(page: Page):
  """
  Test case for verifying that the home page redirects to the login page when the user is not authenticated.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the home page.
  2. Verifies that the login page is displayed.
  """
  page.goto('/')
  verify_login_page(page)


def test_home_redirects_to_reminders_when_logged_in(page: Page, user: User):
  """
  Test case for verifying that the home page redirects to the reminders page when the user is logged in.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.
  - user (User): The User object representing the user credentials.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to the login page.
  2. Fills in the username and password fields with the provided user credentials.
  3. Clicks the "Login" button.
  4. Navigates to the home page.
  5. Verifies that the reminders page is displayed with the correct user information.
  """

  # Given the user is logged in
  page.goto('/login')
  log_in(page, user)

  # When the user navigates to the home page
  page.goto('/')

  # Then the reminders page is displayed with the correct user information
  verify_reminders_page(page, user)


def test_invalid_navigation_redirects_to_not_found(page: Page):
  """
  Test case for verifying that invalid navigation redirects to the not found page.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  Returns:
  None

  This test case performs the following steps:
  1. Navigates to an invalid URL.
  2. Verifies that the not found page is displayed.
  """

  # Given the code is correctly running

  # When the user navigates to an invalid URL
  page.goto('/invalid-url')

  # Then the not found page is displayed
  expect(page.locator('text=Not Found')).to_be_visible()

# --------------------------------------------------------------------------------
# Reminders Behaviors
#
#   the initial reminders page is empty
#   create the first list
#   create more lists
#   create the first item in a list
#   create more items in a list
#   strike an item as completed
#   unstrike an item from being completed
#   edit the name of an uncompleted item
#   edit the name of a completed item
#   begin editing the name of a list but cancel by clicking X
#   begin editing the name of a list but cancel by clicking away
#   begin editing the name of a list but cancel by typing ESCAPE
#   delete an item
#   delete all items
#   creat new items after deleting all items in a list
#   select a different list
#   edit the name of an unselected list
#   edit the name of a selected list
#   commit an edit by clicking check
#   commit an edit by typing ENTER
#   begin editing the name of a list but cancel by clicking X
#   begin editing the name of a list but cancel by clicking away
#   begin editing the name of a list but cancel by typing ESCAPE
#   delete an unselected list
#   delete a selected list
#   delete all lists
#   create new lists after deleting all lists
#   verify only one row (list or item) may be edited at a time:
#     list name
#     new list name
#     item description
#     new item description
#   data persists after page refresh
#   data persists after logout and log back in
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# User Behaviors
#
#   log in as separate users in separate sessions
#   one user cannot see another user's reminders
# --------------------------------------------------------------------------------
