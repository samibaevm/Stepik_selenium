from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()
    new_window = browser.window_handles[1]
    old_wndow = browser.window_handles[0]
    browser.switch_to.window(new_window)
    value = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(value)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > button').click()


finally:
    time.sleep(10)
    browser.quit()
