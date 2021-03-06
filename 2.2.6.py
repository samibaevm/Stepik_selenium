import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://SunInJuly.github.io/execute_script.html')
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(x)
    browser.execute_script("window.scrollBy(0, 120);")
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'body > div.container > form > button').click()

finally:
    time.sleep(10)
    browser.quit()
