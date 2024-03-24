from infra.infra_api.api_wrapper import OtakuAPI


class LoginPage(OtakuAPI):
    def __init__(self):  # Constructor method to initialize class attributes
        super().__init__()
        self.json = None

    def get_login_page(self):
        return self.api_get_request(f'{self.url}login')

    def login_user_to_account(self, mail, password):
        self.json = {"username": mail, "password": password}
        self.response = self.request.post(f'{self.url[:-2]}api/users/login/', json=self.json)
        return self.response.status_code

    def register_account(self, username, mail, password):
        self.json = {"name": username, "email": mail, "password": password}
        self.response = self.request.post(f'{self.url[:-2]}api/users/register/', json=self.json)
        return self.response.status_code


