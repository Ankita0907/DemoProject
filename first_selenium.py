import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org//selenium-python-tutorial//")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.close()




