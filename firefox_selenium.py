from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Firefox()

driver.get("https://www.amazon.in/")
time.sleep(5)
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@id='nav-logo-sprites']").click()

print(driver.title)



