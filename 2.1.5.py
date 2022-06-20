from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x_el):
    return str(math.log(abs(12 * math.sin(int(x_el)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y= calc(x_element)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, 'body > div.container > form > button').click()

finally:
    time.sleep(10)
    browser.quit()
