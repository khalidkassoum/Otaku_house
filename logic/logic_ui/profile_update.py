import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.infra_ui.base_page import BasePage
from infra.infra_ui.handle import Handler


class UpdatingProfile(BasePage):
    user_button=(By.ID,'username')
    profile_button=(By.LINK_TEXT,'Profile')
    details_button=(By.LINK_TEXT,'DETAILS')
    user_name_input=(By.ID, "name")
    mail_input=(By.ID, "email")
    password_input=(By.ID,"password")
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def click_username(self):
        name_button = self.wait.until(EC.element_to_be_clickable(self.user_button))
        name_button.click()


    def click_profile(self):
        prfile = self.wait.until(EC.element_to_be_clickable(self.profile_button))
        prfile.click()


    def validate_success_message_update_name(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((self.user_name_input))).text
        return success_message_text

    def validate_success_message_update_mail(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((self.mail_input))).text
        return success_message_text

    def validate_success_message_update_password(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((self.password_input))).text
        return success_message_text

    def update_flow(self):

        self.click_username()
        self.click_profile()



