import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.infra_ui.base_page import BasePage
from infra.infra_ui.handle import Handler


class Place_order(BasePage):
    user_button=(By.ID,'username')
    profile_button=(By.LINK_TEXT,'Profile')
    details_button=(By.LINK_TEXT,'DETAILS')
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
        self.driver.execute_script("window.scrollTo(300, document.body.scrollHeight);")
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_details(self):
       det_button = self.wait.until(EC.element_to_be_clickable(self.details_button))
       det_button.click()

    # def validate_success_message(self):
    #     success_message_text = self.wait.until(
    #         EC.visibility_of_element_located((self.my_review))).text
    #     return success_message_text



    def place_flow(self):

        self.click_username()
        self.click_profile()
        self.click_details()


