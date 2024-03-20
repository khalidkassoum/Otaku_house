# import time
#
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from infra.base_page import BasePage
#
# class ReviewMyItem(BasePage):
#
#     item_img=(By.CLASS_NAME,'card-img')
#
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def click_login(self):
#         item_button = self.wait.until(EC.element_to_be_clickable(self.item_img))
#         item_button.click()
#
#     def email_input(self):
#
#         email_window = self.wait.until(EC.visibility_of_element_located(self.emaill_button))
#         email_window.clear()
#         email_window.send_keys("khalidkassom59@gmail.com")
#         email_window.send_keys(Keys.RETURN)
#         time.sleep(5)
#
#     def password_input(self):
#         email_window = self.wait.until(EC.visibility_of_element_located(self.passwordd_button))
#         email_window.clear()
#         email_window.send_keys("khalid@22")
#         email_window.send_keys(Keys.RETURN)
#         time.sleep(5)
#
#     def click_signIn(self):
#         sign_element = self.wait.until(EC.element_to_be_clickable(self.sign_button))
#         sign_element.click()
#
#
#     def login_flow(self):
#         self.click_login()
#         self.email_input()
#         self.password_input()
#         self.click_signIn()
#
