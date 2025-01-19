import os
from board_api.crud import api



def test_get_single_user_info():
    user_ids = os.getenv('USER_ID')
    response = api.get_single_user(user_ids)
    status_code = response[1]
    assert response[0]['data']["email"] == os.getenv('USER_EMAIL')
    assert response[0]['data']['first_name'] == os.getenv('USER_FIRST_NAME')
    assert response[0]['data']['last_name'] == os.getenv('USER_LAST_NAME')
    assert status_code == 200
