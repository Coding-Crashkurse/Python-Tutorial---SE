from unittest.mock import patch
import pytest
from script import is_adult, User


def test_is_adult():
    assert is_adult(20) == True
    assert is_adult(15) == False


def test_user_get_age():
    user = User(25)
    assert user.get_age() == 25


def test_user_get_age_with_mock():
    with patch("script.User.get_age", return_value=30):
        user = User(25)
        assert user.get_age() == 30
