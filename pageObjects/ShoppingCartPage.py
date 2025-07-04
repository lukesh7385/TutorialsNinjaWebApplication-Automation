from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC


class ShoppingCartPage:
    shoppingCartHeaderOption = (By.XPATH, "//span[normalize-space()='Shopping Cart']")


    def __init__(self, driver):
        self.driver = driver

    def click_on_shopping_cart_header_option(self):
        shopping_cart_header_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(ShoppingCartPage.shoppingCartHeaderOption)
        )
        shopping_cart_header_option.click()