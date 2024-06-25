'''
Automating dropdowns (also known as select elements) in Selenium with Python involves several steps to interact with
and manipulate these dropdown menus on webpages. Dropdowns in HTML can be implemented using <select> and <option> tags.
Guide on how to automate dropdowns in Selenium with Python:-
Prerequisites:
Ensure you have the necessary imports from Selenium:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

Example HTML Dropdown:
Consider a simple HTML dropdown on a webpage:
<select id="dropdown">
    <option value="option1">Option 1</option>
    <option value="option2">Option 2</option>
    <option value="option3">Option 3</option>
</select>

Automation Steps:
1. Locate the Dropdown Element:
SYNTAX-:
# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the webpage with the dropdown
driver.get("https://example.com")

# Find the dropdown element by ID (or any other suitable locator)
dropdown = driver.find_element(By.ID, "dropdown")

2. Interact with the Dropdown Using Selenium's Select Class:
Selenium provides the Select class specifically for interacting with dropdowns:
# Create a Select object
dropdown_select = Select(dropdown)

3) Dropdown Operations:

a) Selecting Options:
By Visible Text:   dropdown_select.select_by_visible_text("Option 2")
By Value:          dropdown_select.select_by_value("option3")
By Index(0 Based):  dropdown_select.select_by_index(0)
Deselecting option( If Multi-Select Dropdown):  dropdown_select.deselect_all()

4) Handling Multiple Select Dropdowns:
If the dropdown allows multiple selections (<select multiple>), you can use select_by_* methods multiple times or
iterate over options:

dropdown_select = Select(driver.find_element(By.ID, "multiple_dropdown"))
# Selecting options
dropdown_select.select_by_visible_text("Option 1")
dropdown_select.select_by_visible_text("Option 3")

# Deselecting options
dropdown_select.deselect_by_visible_text("Option 1")

5) Assertions and Validations:
Verify the selected option or other properties of the dropdown:
# Get the currently selected option
selected_option = dropdown_select.first_selected_option.text
assert selected_option == "Option 2", f"Expected 'Option 2' but got '{selected_option}'"

6) Close the WebDriver:
Always close the WebDriver session when done:  driver.quit()






'''