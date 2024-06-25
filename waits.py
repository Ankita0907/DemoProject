'''
In Selenium with Python, waiting refers to the technique of pausing the execution of your script until a certain condition is met.
This is crucial in web automation because web pages can load asynchronously, and elements may not be immediately available or interactive.
Types of Waits in Selenium with Python:

1) Implicit Wait:
Usage: Use implicit waits to wait for elements that may not appear immediately or to handle cases
where elements might take some time to load after a page is loaded.
syntax-:
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be found

driver.get("https://example.com")
element = driver.find_element_by_id("myElement")

2) Explicit Wait (WebDriverWait):
Explicit waits allow you to wait for a certain condition to occur before proceeding with execution.
Use explicit waits when you need to wait for specific conditions like element visibility, presence, or clickability.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myElement"))
    )
    element.click()

except TimeoutException:
    print("Element not found within 10 seconds")

finally:
    driver.quit()

3) Fluents wait-:
Use fluent waits when you need to wait for an element with a dynamic loading pattern or
when you need to customize the wait conditions extensively.
syntax-:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import FluentWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://example.com")

wait = FluentWait(driver, timeout=30, poll_frequency=5,
                  ignored_exceptions=[NoSuchElementException, TimeoutException])

element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))
element.click()

driver.quit()

Common Use Cases for Waiting in Selenium:
Waiting for Element Visibility
Waiting for Element Clickability
Waiting for Page Load
Waiting for Dynamic Elements











'''