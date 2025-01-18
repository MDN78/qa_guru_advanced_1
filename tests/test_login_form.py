from board_api.crud import api
import pytest
import os


@pytest.mark.skip
def test_successful_registration():
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    user_info = api.registration_user(email, password)
    user_id = user_info[0]
    status_code = user_info[1]
    assert user_id == os.getenv('USER_ID')
    assert status_code == 200


@pytest.mark.skip
def test_unsuccessful_registration():
    email = os.getenv('USER_EMAIL')
    user_info = api.unsuccessful_registration_user(email)
    status = user_info[0]
    status_code = user_info[1]
    assert status['error'] == "Missing password"
    assert status_code == 400


@pytest.mark.skip
def test_login_user():
    email = os.getenv('USER_EMAIL')
    password = os.getenv('USER_PASSWORD')
    login_user_info = api.login_user(email, password)
    status_code = login_user_info[1]
    user_token = login_user_info[0]
    assert status_code == 200
    assert len(user_token) > 0
