from board_api.crud import api
import os


def test_create_new_user():
    name = os.getenv('NEW_USER_NAME')
    job = os.getenv('NEW_USER_JOB')
    new_user = api.create_new_user(name, job)
    status_code = new_user[1]
    assert status_code == 201
    assert new_user[0]["name"] == name


def test_update_user_info():
    name = os.getenv('NEW_USER_NAME')
    job = os.getenv('NEW_USER_JOB')
    user_id = os.getenv('USER_ID')
    new_user = api.update_user_info(name, job, user_id)
    status_code = new_user[1]
    assert status_code == 200
    assert new_user[0]["name"] == name


def test_delete_user_by_id():
    delete_user = api.delete_user()
    status_code = delete_user[1]
    assert delete_user[0] == 'deleted'
    assert status_code == 204
