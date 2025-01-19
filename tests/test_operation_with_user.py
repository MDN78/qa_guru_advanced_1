import os
from board_api.crud import api


def test_create_new_user():
    name = os.getenv('NEW_USER_NAME')
    job = os.getenv('NEW_USER_JOB')
    new_user = api.create_new_user(name, job)
    print(new_user)
    status_code = new_user[1]
    assert status_code == 201
    assert new_user[0]["name"] == name


def test_update_user_info():
    name = os.getenv('NEW_USER_NAME')
    job = os.getenv('NEW_USER_JOB')
    new_user = api.update_user_info(name, job)
    status_code = new_user[1]
    assert status_code == 200
    assert new_user[0]["name"] == name
