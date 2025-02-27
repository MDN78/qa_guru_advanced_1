import requests


class ReqresApi:

    def __init__(self, url):
        self.url = url

    def get_single_user(self, user_id: str) -> list:
        resp = requests.get(f'{self.url}users/{user_id}')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def create_new_user(self, name: str, job: str) -> list:
        payload = {
            "name": name,
            "job": job
        }
        resp = requests.post(f'{self.url}users', params=payload)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def update_user_info(self, name: str, job: str, user_id=2) -> list:
        payload = {
            "name": name,
            "job": job,
        }
        resp = requests.put(f'{self.url}users/{user_id}', params=payload)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def delete_user(self, user_id=2) -> list:
        resp = requests.delete(f'{self.url}users/{user_id}')
        status_code = resp.status_code
        status = f'{resp.text}deleted'
        return [status, status_code]

    def login_user(self, email: str, password: str) -> list:
        payload = {
            'email': email,
            'password': password
        }
        resp = requests.post(f'{self.url}login', json=payload)
        status_code = resp.status_code
        user_token = resp.json()['token']
        return [user_token, status_code]


api = ReqresApi("http://127.0.0.1:8000/api/")
