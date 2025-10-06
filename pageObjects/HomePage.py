from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    continueShoppingBTN = (By.LINK_TEXT, "Continue Shopping")
    pcZeroOption = (By.XPATH, "//a[normalize-space()='PC (0)']")


    def __init__(self, driver):
        self.driver = driver

    def click_on_continue_shopping_button(self):
        continue_shopping_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(HomePage.continueShoppingBTN)
        )
        continue_shopping_button.click()

    def pc_zero_product_option(self):
        zero_product_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
        EC.element_to_be_clickable(HomePage.pcZeroOption)
    )
        zero_product_option.click()



