import unittest

from logic.logic_api.update_profile_api import UpdateProfile


class TestOtakuHouseProfilePage(unittest.TestCase):

    def setUp(self):
        self.myProfile = UpdateProfile()
        self.response = None
        self.data = None

    def test_update_profile_name(self):
        self.response = self.myProfile.profileUpdating(self.myProfile.user_id, self.myProfile.new_Name, self.myProfile.user_mail, self.myProfile.user_password)
        self.assertEqual(self.response.status_code, 200)


    def test_update_profile_mail(self):
        self.response = self.myProfile.profileUpdating(self.myProfile.user_id, self.myProfile.user_name,
                                                         self.myProfile.new_mail,
                                                         self.myProfile.user_password)
        self.assertEqual(self.response.status_code, 200)

    def test_update_profile_password(self):
        self.response = self.myProfile.profileUpdating(self.myProfile.user_id, self.myProfile.user_name,
                                                         self.myProfile.user_mail,
                                                         self.myProfile.new_password)
        self.assertEqual(self.response.status_code, 200)

    # def test_getting_order_dietels(self):
    #     self.response = self.profile_page.get_order_dietels(self.profile_page.order_id)
    #     self.assertEqual(self.response.status_code, 200)
