import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

# Replace the file path with the correct one and escape backslashes
file_path = r"C:\Users\sriva\OneDrive\Desktop\Web\new.html"

# Open the local HTML file
driver.get("file:///" + file_path)

# Maximize the browser window
driver.maximize_window()
time.sleep(2)
'''
name = driver.find_element(By.XPATH, "//input[@id='username']").send_keys('Ankita')
time.sleep(1)

password =  driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Ankisweet27')
time.sleep(1)

dropdown= driver.find_element(By.XPATH, "//select[@id='country']")
select = Select(dropdown)
select.select_by_visible_text('Australia')
time.sleep(1)

birthdate_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "birthdate")))
birthdate_input.clear()
birthdate_input.send_keys("06-21-2023")
time.sleep(1)

gender_selection = driver.find_element(By.XPATH,"//input[@value='female']").click()
time.sleep(1)

newsletter_checkbox = driver.find_element(By.XPATH,"//input[@id='newsletter']").click()
time.sleep(1)

terms_checkbox = driver.find_element(By.XPATH,"//input[@id='terms']").click()
time.sleep(1)

submit_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)
'''

name = (driver.find_element(By.XPATH, "//input[@id='username']"))
name.send_keys('Ankita')
time.sleep(1)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys('teammemberhbi')
time.sleep(1)

dropdown= driver.find_element(By.XPATH, "//select[@id='country']")
select = Select(dropdown)
select.select_by_visible_text('Australia')
time.sleep(1)

#birthdate was not clickable
birthdate_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "birthdate")))
birthdate_input.clear()
birthdate_input.send_keys("06-21-2023")
time.sleep(1)

gender_selection = driver.find_element(By.XPATH,"//input[@value='female']").click()
time.sleep(1)

newsletter_checkbox = driver.find_element(By.XPATH,"//input[@id='newsletter']").click()
time.sleep(1)

terms_checkbox = driver.find_element(By.XPATH,"//input[@id='terms']").click()
time.sleep(1)


name.clear()
time.sleep(3)
name.send_keys('Mohan Singh Ankita')
time.sleep(1)
password.clear()
time.sleep(3)
password.send_keys('Ankita')
time.sleep(1)

submit_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()



