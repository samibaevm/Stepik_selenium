from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    btn_1 = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()



finally:
    time.sleep(10)
    browser.quit()