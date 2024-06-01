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
  4. Asserts that the page title is "Reminders | Bulldoggy reminders app".
  5. Asserts that the URL matches the expected pattern.
  6. Asserts that the "bulldoggy-logo" element is visible.
  7. Asserts that the "bulldoggy-title" element has the text "Bulldoggy".
  8. Asserts that the "Logout" button is visible.
  9. Asserts that the "reminders-message" element displays "Reminders for" followed by the user's username.

  Note: This test case assumes the presence of the Playwright library and the necessary setup for running browser tests.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user logs into the app with valid credentials
  page.locator('[name="username"]').fill(user.username)
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # Then the reminders page is displayed
  expect(page).to_have_title('Reminders | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'reminders'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.locator('id=bulldoggy-title')).to_have_text('Bulldoggy')
  expect(page.get_by_role('button', name='Logout')).to_be_visible()

  # And the reminders page title card displays "Reminders for" the user's username
  expect(page.locator('id=reminders-message')).to_have_text(f'Reminders for {user.username}')

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
  3. Asserts that the page title is "Login | Bulldoggy reminders app".
  4. Asserts that the URL matches the expected pattern.
  5. Asserts that the "bulldoggy-logo" element is visible.
  6. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no login credentials
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()

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
  4. Asserts that the page title is "Login | Bulldoggy reminders app".
  5. Asserts that the URL matches the expected pattern.
  6. Asserts that the "bulldoggy-logo" element is visible.
  7. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no username
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()

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
  4. Asserts that the page title is "Login | Bulldoggy reminders app".
  5. Asserts that the URL matches the expected pattern.
  6. Asserts that the "bulldoggy-logo" element is visible.
  7. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides no password
  page.locator('[name="username"]').fill(user.username)
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()

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
  4. Asserts that the page title is "Login | Bulldoggy reminders app".
  5. Asserts that the URL matches the expected pattern.
  6. Asserts that the "bulldoggy-logo" element is visible.
  7. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides incorrect username, but correct password
  page.locator('[name="username"]').fill('invalid-username')
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()
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
  4. Asserts that the page title is "Login | Bulldoggy reminders app".
  5. Asserts that the URL matches the expected pattern.
  6. Asserts that the "bulldoggy-logo" element is visible.
  7. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')

  # When the user provides correct username, but incorrect password
  page.locator('[name="username"]').fill(user.username)
  page.locator('[name="password"]').fill('invalid-password')
  page.get_by_text('Login').click()

  # Then the error message is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()
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
  5. Asserts that the page title is "Login | Bulldoggy reminders app".
  6. Asserts that the URL matches the expected pattern.
  7. Asserts that the "bulldoggy-logo" element is visible.
  8. Asserts that the "Login" button is visible.
  """
  # Given the login page is displayed
  page.goto('/login')
  page.locator('[name="username"]').fill(user.username)
  page.locator('[name="password"]').fill(user.password)
  page.get_by_text('Login').click()

  # When the user clicks the logout button
  page.get_by_text('Logout').click()

  # Then the login page is displayed
  expect(page).to_have_title('Login | Bulldoggy reminders app')
  expect(page).to_have_url(re.compile(re.escape('/') + 'login'))
  expect(page.locator('id=bulldoggy-logo')).to_be_visible()
  expect(page.get_by_role('button', name='Login')).to_be_visible()
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
