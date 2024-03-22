import unittest
from logic.logic_api.search_item import SearchItem
class TestOtakuHouseHomePage(unittest.TestCase):

    def setUp(self):
        self.search = SearchItem()
        self.response = None
        self.data = None

    def test_search_item(self):
        self.response = self.search.search_ITEM(self.search.searching_keyword)
        self.assertEqual(self.response.status_code, 200)

