import unittest
from logic.login_logic import LoginPage
from logic.review_item_api import OtakuReviewItem
from logic.place_order_api import PlaceOrder



class Test_place_order(unittest.TestCase):

    def setUp(self):
        self.place_order= PlaceOrder()
        self.response = None
        self.data = None

    def test_place_order(self):
        self.response = self.place_order.place_Order()
        self.assertEqual(self.response.status_code, 200)