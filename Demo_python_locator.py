import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.get("https://www.amazon.com/")
driver.maximize_window()
time.sleep(2)
element = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iphone 15")
button = driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

