from logic.logic_ui.review_item_UI import ReviewMyItem
from tests.tests_ui.test import GridTest
from infra.infra_api.Handle_api import Handler_api
class gridtest_review(GridTest):

    def review_product(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.myReview=ReviewMyItem(self.driver)
        self.myReview.review_flow()
        self.myhandler=Handler_api()
        self.config=self.myhandler.read_config_data()
        assert self.config['review_text'] in (self.myReview.validate_success_message())



    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.review_product)
        else:
            self.browser.test_run_grid_serial(self.review_product)
