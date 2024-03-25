import unittest
from tests.tests_api.placeOrder_api import Test_place_order
from tests.tests_ui.place_order_ui import gridtest_PlaceOrder
from tests.tests_api.review_item_api import TestReview_item_test
from tests.tests_ui.review_ITEMM_UI import gridtest_review
from tests.tests_api.updateProfile_testAPI import TestOtakuHouseProfilePage
from tests.tests_ui.UPDATEprofile_test import gridtest_update

def test_run_suite():
 suite = unittest.TestSuite()
 suite.addTest(unittest.makeSuite(Test_place_order))
 suite.addTest(unittest.makeSuite(gridtest_PlaceOrder))
 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(suite)

def test_run_second_suite():
 second_suite = unittest.TestSuite()
 second_suite.addTest(unittest.makeSuite(TestReview_item_test))
 second_suite.addTest(unittest.makeSuite(gridtest_review))
 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(second_suite)

def test_run_third_suite():
 third_suite = unittest.TestSuite()
 third_suite.addTest(unittest.makeSuite(TestOtakuHouseProfilePage))
 third_suite.addTest(unittest.makeSuite(gridtest_update))
 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(third_suite)

if __name__ == "__main__":
    test_run_suite()
    # test_run_second_suite()
    # test_run_third_suite()

