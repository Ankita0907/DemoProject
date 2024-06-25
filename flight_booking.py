import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise//")
driver.maximize_window()
time.sleep(2)

country_select = driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys('INDIA')
time.sleep(1)
trip_type= driver.find_element(By.XPATH,"//input[@id='ctl00_mainContent_rbtnl_Trip_1']").click()
time.sleep(1)
#departure
departure_dropdown= driver.find_element(By.XPATH,"//span[@id='ctl00_mainContent_ddl_originStation1_CTXTaction']").click()
time.sleep(1)
departure_elements = driver.find_elements(By.XPATH, "//input[@id='ctl00_mainContent_ddl_originStation1_CTXT']")
# Check if there are multiple elements

if len(departure_elements) > 0:
    # Click the first element (index 0)
    departure_elements[0].send_keys("Delhi")
else:
    print("No elements found with the given XPath")
time.sleep(1)
#arrival
arrival_dropdown= driver.find_element(By.XPATH,"//span[@id='ctl00_mainContent_ddl_destinationStation1_CTXTaction']")
time.sleep(1)
departure_elements = driver.find_elements(By.XPATH, "//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']")
# Check if there are multiple elements

if len(departure_elements) > 0:
    # Click the first element (index 0)
    departure_elements[0].send_keys("Goa")
else:
    print("No elements found with the given XPath")
time.sleep(1)

# departure date(when the date is clickable)
date_elements = driver.find_elements(By.XPATH, "//td[@data-month='5']")
# Iterate through each date element
for i in date_elements:
    # Retrieve the text of the element
    date_text = i.text
    # Print the text for debugging
    print("Date text:", date_text)
    # Check if the text is "27"
    if date_text == "27":
        # Click on the element if the text is "27"
        i.click()
        time.sleep(1)
        print("Clicked on date 27")
        break

# return date(when the date is clickable)
date_elements = driver.find_elements(By.ID, "view_fulldate_id_2")
# if len(departure_elements) > 0:
#     # Click the first element (index 0)
#     departure_elements[0].click()
# else:
#     print("No elements found with the given XPath")
time.sleep(1)
# Iterate through each date element
for j in date_elements:
    # Retrieve the text of the element
    date_text = j.text
    # Print the text for debugging
    print("Date text:", date_text)
    # Check if the text is "30"
    if date_text == "30":
        # Click on the element if the text is "30"
        j.click()
        time.sleep(1)
        print("Clicked on date 30")
        break

#passenger details
# Find all elements matching "//div[text()='1 Adult']"
passenger = driver.find_elements(By.XPATH, "//div[text()='1 Adult']")

try:
    # Wait for passenger element to be clickable
    passenger = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='1 Adult']")))
    passenger.click()

    # Wait for add adult element to be clickable
    add_adult = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='hrefIncAdt']")))
    add_adult.click()

    # Add a small delay to ensure the click action is registered
    time.sleep(1)

finally:
    driver.quit()

#currency dropdown
# currency_dropdown = driver.find_elements(By.XPATH, "//select[@id='ctl00_mainContent_DropDownListCurrency']")
# currency_dropdown.click()
# time.sleep(2)

# add_currency = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='ctl00_mainContent_DropDownListCurrency']/option[2]")))
# add_currency.click()
# time.sleep(2)

#search_button

# submit_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='ctl00_mainContent_btn_FindFlights']")))
# submit_button.click()
# time.sleep(2)
submit_button = driver.find_element(By.XPATH,"//input[@id='ctl00_mainContent_btn_FindFlights']").click()