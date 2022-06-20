from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    num1 = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    Select(browser.find_element(By.CSS_SELECTOR, '#dropdown')).select_by_value(str(num1 + num2))
    browser.find_element(By.CLASS_NAME, 'btn ').click()

finally:
    time.sleep(2)
    browser.quit()
