from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()
time.sleep(2)
search_bar= driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
search_bar.send_keys('iphone15')
search_button= driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']")
search_button.click()
first_search_element= driver.find_element(By.XPATH,"//img[@class='s-image s-image-optimized-rendering'][@alt='Sponsored Ad - Apple iPhone 15 (128 GB) - Black']")
first_search_element.click()
add_to_cart_button= driver.find_element(By.XPATH,"(//input[@name='submit.add-to-cart'][@aria-labelledby='submit.add-to-cart-announce'][@id='add-to-cart-button']['2']")
add_to_cart_button.click()
print('Item added successfully')

