from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_guides_search_page(self):
        guides_search_link = self.browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/ul/li[1]/a")
        guides_search_link.click()
