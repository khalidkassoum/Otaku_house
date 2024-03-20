import requests


class AuthAPI:
    BASE_URL = 'http://127.0.0.1:8000/#/'  # This would be the base URL for your API

    @staticmethod
    def login(email, password):
        login_url = f'{AuthAPI.BASE_URL}/login'
        payload = {'email': 'khalidkassom59@@gmail.com', 'password':'khalid@22' }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(login_url, data=payload, headers=headers)
        return response
