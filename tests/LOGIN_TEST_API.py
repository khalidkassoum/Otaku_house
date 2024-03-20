import unittest
from logic.loginPageAPI import AuthAPI
from logic.loginPageUI import loginPage
from tests.test import GridTest


class TestAuthAPI(GridTest):

    def test_login_success(self, cap):
       # self.driver = self.browser.get_driver(cap)
        response = AuthAPI.login('khalidkassom59@@gmail.com', 'khalid@22')
        self.assertEqual(response.status_code, 200)


    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_login_success)
        else:
            self.browser.test_run_grid_serial(self.test_login_success)




