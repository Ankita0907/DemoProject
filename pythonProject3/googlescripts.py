from selenium import webdriver

a= webdriver.Chrome()
a.get("http://www.google.com")
mypagetitle= a.title
assert "Google" in mypagetitle
a.quit()
