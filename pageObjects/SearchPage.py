from selenium.webdriver.common.by import By


class SearchPage:

    textBox_searchField = (By.XPATH, "//input[@name='search' and @type='text']")
    button_search = (By.XPATH, "//button[@class='btn btn-default btn-lg' and @type='button']")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product):
        self.driver.find_element(*SearchPage.textBox_searchField).send_keys(product)

    def click_on_search_button(self):
        self.driver.find_element(*SearchPage.button_search).click()

