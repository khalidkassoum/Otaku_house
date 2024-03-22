from logic.logic_ui.loginPageUI import loginPage
from test import GridTest
class gridtest_LOGIN(GridTest):

    def test_login(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.Mylogin = loginPage(self.driver)
        self.Mylogin.login_flow()


    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_login)
        else:
            self.browser.test_run_grid_serial(self.test_login)
