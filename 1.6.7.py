from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("sdafdsfsfsafsfsafsfsdfsfsafsdfsdfsafsdfsdfsafsdfasfsfsdf")

    browser.find_element(By.CSS_SELECTOR, "Button.btn").click()

finally:
    time.sleep(30)
    browser.quit()




