from  locators import MainPageLocators
from locators import GuideLocator
from selenium import webdriver
from selenium.webdriver.common.by import By
""""
browser = webdriver.Chrome()
browser.get("https://www.izi.travel/en")
b = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/ul/li[1]/a")
b.click()
"""
browser = webdriver.Chrome()
browser.get("https://www.izi.travel/en")
b = browser.find_element(By.XPATH, GuideLocator.a)
b.click()
#print(b)