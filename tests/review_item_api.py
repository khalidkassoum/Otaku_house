import unittest
from logic.login_logic import LoginPage
from logic.review_item_api import OtakuReviewItem


class TestReview_item_test(unittest.TestCase):

    def setUp(self):
        self.otaku_house_review = OtakuReviewItem()
        self.otaku_house=LoginPage()
        self.response = None
        self.data = None


    def test_get_product_page(self):
        self.response = self.otaku_house_review.get_product_page(self.otaku_house_review.product_id)
        self.assertEqual(self.response.status_code, 200)

    def test_review_item(self):
        self.response = self.otaku_house_review.choosing_product(self.otaku_house_review.rating,self.otaku_house_review.review_txt,self.otaku_house_review.product_id)
        self.assertEqual(self.response.status_code, 200)
