from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_guides_search_page(self):
        guides_search_link = self.browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/ul/li[1]/a")
        guides_search_link.click()


    def should_be_audio_guides_link(self):
        assert self.is_element_present(*MainPageLocators.audio_guides_link), "Audio guides link is not presented"