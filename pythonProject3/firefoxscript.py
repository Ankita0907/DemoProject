from selenium import webdriver
firefox=webdriver.Firefox()
firefox.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
print(firefox.title)
print(firefox.current_url)
firefox.quit()