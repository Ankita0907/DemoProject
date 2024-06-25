from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://example.com")

try:
    # Find all links on the webpage
    links = driver.find_elements(By.TAG_NAME, "a")

    # Print the total number of links
    print(f"Total number of links on the webpage: {len(links)}")

except Exception as e:
    print(f"Error: {e}")

# Close the WebDriver
driver.quit()
