import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.infra_ui.base_page import BasePage
from infra.infra_ui.handle import Handler


class ReviewMyItem(BasePage):

    search_window=(By.NAME,'q')
    img_product=(By.CLASS_NAME,'card-img')
    my_review=(By.XPATH,"//input[@class='list-group-item' and .//strong[text()='khalid kassom']]")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_product(self):
        item_button = self.wait.until(EC.element_to_be_clickable(self.img_product))
        item_button.click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def validate_success_message(self):
        success_message_text = self.wait.until(
            EC.visibility_of_element_located((self.my_review))).text
        return success_message_text


    def search_input(self):
        myjson = Handler()
        name_of_product = myjson.config['product_name']
        searchh = self.wait.until(EC.visibility_of_element_located(self.search_window))
        searchh.clear()
        searchh.send_keys(name_of_product)
        searchh.send_keys(Keys.RETURN)
        time.sleep(5)


    def review_flow(self):
        self.search_input()
        self.click_product()


