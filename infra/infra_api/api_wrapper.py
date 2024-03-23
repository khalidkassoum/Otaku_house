from json.decoder import JSONDecodeError
import requests
from infra.infra_api.Handle_api import Handler_api
class OtakuAPI:

   def __init__(self):
        self.response = None
        self.myHandler = Handler_api()
        self.config = self.myHandler.read_config_data()
        self.url = self.config['url']
        self.user_name = self.config['user_name']
        self.user_mail = self.config['login_mail']
        self.user_password = self.config['login_password']
        self.searching_keyword = self.config['keyword_for_search'].lower()
        self.product_id = self.config['product_id']
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzA3MDczLCJqdGkiOiI2MTVhNWM1MTljOGQ0MmFjODM4YWI0MGExYzg2YTE2ZSIsInVzZXJfaWQiOjh9.dpK02iVtvtLn2VeZkFRngY4pWzYvGzUj34F1uYZRJis"
        self.headers= {
            "Authorization": f"Bearer {self.token}"
        }
        self.token2="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzEyOTE5LCJqdGkiOiI5MGQ3NmJhM2Q1YTg0MTE4ODFiN2UxZGNmODllMGI0YiIsInVzZXJfaWQiOjh9.JmN9m1-qwAduAGmA7XGuoFERJvCdQLhf_XHqeIu5IEA"
        self.headers2 = {
             "Authorization": f"Bearer {self.token2}"
        }
        self.updateProfileToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzk3NzgxLCJqdGkiOiI1MjFjYTM5MWIxODE0ZDkyYjhiMDZjMjZjYWVhMjY2MyIsInVzZXJfaWQiOjh9.N2DQiPUUNLlvR1i2bD5oY8rVdcohs764X2qRe67KRXo"
        self.headersUpdate = {
             "Authorization": f"Bearer {self.updateProfileToken}"
        }
        self.rating = self.config['rating_product']
        self.review_txt = self.config['review_text']
        self.order_id = self.config['order_id']
        self.user_id = self.config['user_id']
        self.request = requests
        self.new_Name=self.config['new_username']
        self.new_mail=self.config['new_mail']
        self.new_password=self.config['new_password']
        self.parallel = True

   def api_get_request(self, url):
        self.response = self.request.get(url)
        return self.response



