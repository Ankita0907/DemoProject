'''
In Selenium with Python, filters are typically used to refine or narrow down search criteria when locating elements on a webpage.
Using Filters in Selenium with Python:-

1. Locating Elements with Filters:-
a) By ID:
syntax-: element = driver.find_element(By.ID, "element_id")
b) By CLASS_NAME-
syntax-: elements = driver.find_elements(By.CLASS_NAME, "element_class")
c)By NAME-:
element = driver.find_element(By.NAME, "element_name")
d)By XPath:
element = driver.find_element(By.XPATH, "//div[@id='content']")
e) By CSS Selector:
element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
f)By LINK
g)By PARTIAL_LINK

2) Using Filters for Dynamic Content:
When dealing with dynamic content or elements generated after page interactions (e.g., AJAX),
you may need to use explicit waits combined with filters:
SYNTAX-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for an element with specific ID to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "element_id"))

3) Chaining Filters-
# Find a button inside a specific div
button = driver.find_element(By.XPATH, "//div[@class='container']/button")

4) HANDLING MULTIPLE ELEMENTS-
If you expect multiple elements to match your criteria, use find_elements() and iterate over the results:
# Find all elements with a specific class
elements = driver.find_elements(By.CLASS_NAME, "result-item")
for element in elements:
    print(element.text)

5) DYNAMIC ATTRIBUTE AND TEXT CONTENTS:
# Find an element with a specific attribute value
element = driver.find_element(By.CSS_SELECTOR, "input[data-type='search']")

6) ASSERTIONS AND INTERACTIONS-:
Once you've located elements using filters, you can interact with them (e.g., click, enter text)
or assert conditions (e.g., check visibility, text content) based on your test requirements:

# Click on a button
button = driver.find_element(By.ID, "submit_button")
button.click()

# Assert element visibility
element = driver.find_element(By.XPATH, "//div[@id='message']")
assert element.is_displayed()

############ XPath is more powerful but can be slower, while CSS selectors are faster for simple queries.#########

















'''