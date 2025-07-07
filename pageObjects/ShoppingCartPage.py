from jinja2.nodes import Continue
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC


class ShoppingCartPage:
    shoppingCartHeaderOption = (By.XPATH, "//span[contains(text(),'Shopping Cart')]")
    siteMapFooterOption = (By.LINK_TEXT, "Site Map")
    shoppingCartLink = (By.XPATH, "//a[contains(text(),'Shopping Cart')]")
    removeButton = (By.XPATH, "//i[@class='fa fa-times']")


    def __init__(self, driver):
        self.driver = driver

    def click_on_shopping_cart_header_option(self):
        shopping_cart_header_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(ShoppingCartPage.shoppingCartHeaderOption)
        )
        self.driver.execute_script("arguments[0].click();", shopping_cart_header_option)

    def click_on_site_map_footer_option(self):
        site_map_footer_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(ShoppingCartPage.siteMapFooterOption)
        )
        self.driver.execute_script("arguments[0].click();", site_map_footer_option)

    def click_on_shopping_cart_link(self):
        shopping_cart_link = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(ShoppingCartPage.shoppingCartLink)
        )
        self.driver.execute_script("arguments[0].click();", shopping_cart_link)

    def click_on_remove_button(self):
        remove_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(ShoppingCartPage.removeButton)
        )
        if remove_button:
            remove_button.click()
        else:
            Continue

