from jinja2.nodes import Continue
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC


class ShoppingCartPage:
    shoppingCartHeaderOption = (By.XPATH, "//span[contains(text(),'Shopping Cart')]")
    siteMapFooterOption = (By.LINK_TEXT, "Site Map")
    shoppingCartLink = (By.XPATH, "//a[contains(text(),'Shopping Cart')]")
    removeButton = (By.XPATH, "//i[@class='fa fa-times']")
    quantityField = (By.CSS_SELECTOR, "input[value='1']")
    updateButton = (By.XPATH, "//button[@type='submit']")
    removeIcon = (By.XPATH, "//button[@class='btn btn-danger']")
    emptyShoppingCartMessage = (By.XPATH, "//div[@id='content']//p[contains(text(),'Your shopping cart is empty!')]")


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
        remove_button = WebDriverWait(self.driver, 3, poll_frequency=1).until(
            EC.presence_of_element_located(ShoppingCartPage.removeButton)
        )
        if remove_button:
            remove_button.click()
        else:
            Continue

    def set_quantity_of_the_product(self, quantity):
        quantity_field = self.driver.find_element(*ShoppingCartPage.quantityField)
        quantity_field.clear()
        quantity_field.send_keys(quantity)

    def click_on_update_quantity_button(self):
        update_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(ShoppingCartPage.updateButton)
        )
        update_button.click()

    def click_on_remove_icon(self):
        remove_icon = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(ShoppingCartPage.removeIcon)
        )
        self.driver.execute_script("arguments[0].click();", remove_icon)

    def get_empty_shopping_cart_message(self):
        text_message = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(ShoppingCartPage.emptyShoppingCartMessage)
        )
        return text_message.text

