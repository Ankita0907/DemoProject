'''
CSS Selectors offer a concise and efficient way to target elements based on their attributes, IDs, classes,
and other CSS properties.

Basic CSS Selectors:
1) Using ID:
Selects elements with a specific ID attribute.
SYNTAX-:   element = driver.find_element(By.CSS_SELECTOR, "#element_id")

2)Using Class Name:
Selects elements with a specific class attribute.
SYNTAX-:  elements = driver.find_elements(By.CSS_SELECTOR, ".element_class")

3)Using Attribute:
Selects elements based on any attribute.
SYNTAX-:  element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")

4)Using Element Type:
Selects elements based on their HTML tag name.
SYNTAX-:   elements = driver.find_elements(By.CSS_SELECTOR, "div")

5)CSS Selectors Combinations:
Compound Selectors:
Combines multiple selectors to narrow down the search.
SYNTAX-:  element = driver.find_element(By.CSS_SELECTOR, "div.container")

6)Grouping Selectors:
Selects multiple elements matching any of the grouped selectors.
SYNTAX-:    elements = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='email']")

7)Pseudo-Classes and Pseudo-Elements:
Selects elements based on their state or position in the document.
SYNTAX-:  element = driver.find_element(By.CSS_SELECTOR, "input:focus")

8) Advanced CSS Selectors:
Attribute Selectors:
Selects elements based on their attributes and attribute values.

SYNTAX-:  element = driver.find_element(By.CSS_SELECTOR, "a[href^='https']")  # Starts with
element = driver.find_element(By.CSS_SELECTOR, "input[name$='password']")  # Ends with
element = driver.find_element(By.CSS_SELECTOR, "input[name*='user']")  # Contains

Descendant Selectors:
Selects elements that are descendants of another element.

SYNTAX-:   element = driver.find_element(By.CSS_SELECTOR, "div.container input[type='text']")

'''