from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org")
# assert "Python" in driver.title
# print(driver.title)
#
# assert "Welcome to Python.org" in driver.title
driver.quit()
