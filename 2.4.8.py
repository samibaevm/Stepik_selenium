from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait ( browser, 12 ).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price' ), '100')
    )
    browser.find_element(By.CSS_SELECTOR, '#book').click()
    value = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    result = calc(value)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()



finally:
    time.sleep(10)
    browser.quit()