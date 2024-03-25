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

#


