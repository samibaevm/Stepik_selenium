from selenium import webdriver
from selenium.webdriver.common.by import By

#open browser
browser = webdriver.Chrome()

#open link
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

#find button
button = browser.find_element(By.ID, "submit_button")