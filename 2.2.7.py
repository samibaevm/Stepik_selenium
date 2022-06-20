import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    input_f_name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[1]')
    input_f_name.send_keys('name')
    input_l_name = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[2]')
    input_l_name.send_keys('sname')
    input_email = browser.find_element(By.XPATH, '/html/body/div[1]/form/div/input[3]')
    input_email.send_keys('check@mail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'example.txt')
    file_send = browser.find_element(By.XPATH, '//*[@id="file"]').send_keys(file_path)
    submit = browser.find_element(By.XPATH, '/html/body/div[1]/form/button').click()


finally:
    time.sleep(10)
    browser.quit()

