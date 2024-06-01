"""
This module contains unit tests for the Bulldoggy app.
"""

# --------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------
import sys
import os

# Append the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.auth import serialize_token, deserialize_token
from testlib.inputs import User

# --------------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------------

def test_token_serialization(user: User):
  """
  Test the serialization and deserialization of a token for a given user.

  Args:
      user (User): The user object to serialize and deserialize a token for.

  Raises:
      AssertionError: If the generated token is None, not a string, or equal to the user's username.
      AssertionError: If the deserialized username is not equal to the user's username.

  Returns:
      None
  """

  token = serialize_token(user.username)
  assert token
  assert isinstance(token, str)
  assert token != user.username

  username = deserialize_token(token)
  assert username == user.username
