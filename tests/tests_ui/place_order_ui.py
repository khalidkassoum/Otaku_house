from logic.logic_ui.loginPageUI import loginPage
from logic.logic_ui.place_order_UI import Place_order
from test import GridTest
class gridtest_PlaceOrder(GridTest):

    def test_placeOrder(self,cap):

        self.driver = self.browser.get_driver(cap)
        self.Mylogin = loginPage(self.driver)
        self.Mylogin.login_flow()
        self.placee =Place_order(self.driver)
        self.placee.place_flow()


    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.test_placeOrder)
        else:
            self.browser.test_run_grid_serial(self.test_placeOrder)
