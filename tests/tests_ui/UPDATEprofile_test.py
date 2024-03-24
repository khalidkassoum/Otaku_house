from logic.logic_ui.loginPageUI import loginPage
from logic.logic_ui.profile_update import UpdatingProfile
from logic.logic_ui.review_item_UI import ReviewMyItem
from tests.tests_ui.test import GridTest
from infra.infra_api.Handle_api import Handler_api
class gridtest_update(GridTest):

    def update_profile(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.Mylogin = loginPage(self.driver)
        self.Mylogin.login_flow()
        self.myProfile=UpdatingProfile(self.driver)
        self.myProfile.update_flow()
        # self.myhandler=Handler_api()
        # self.config=self.myhandler.read_config_data()
        # assert self.config['new_username'] in (self.myProfile.validate_success_message_update_name())



    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.update_profile)
        else:
            self.browser.test_run_grid_serial(self.update_profile)
