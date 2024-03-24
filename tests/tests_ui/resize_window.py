
from tests.tests_ui.test import GridTest


class TestWindowResize(GridTest):

    def window_resize(self,cap):
        self.driver = self.browser.get_driver(cap)
        self.driver.set_window_size(800, 600)
        new_size = self.driver.get_window_size()
        assert new_size['width'] == 800
        assert new_size['height'] == 600



    def test_run_MyTest(self):

        self.grid = self.browser.get_grid()
        if self.grid:
            self.browser.test_run_grid_parallel(self.window_resize)
        else:
            self.browser.test_run_grid_serial(self.window_resize)

