from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestPlan():
    def test_first_login(self):
        link = "http://suninjuly.github.io/registration1.html"

        # try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('Manu')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('check@mail.com')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('Samib')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        text1 = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        text2 = "Congratulations! You have successfully registered!"

        assert text1 == text2, "Failed"

    def test_second_login(self):
        link = "http://suninjuly.github.io/registration2.html"

            # try:
        browser = webdriver.Chrome()
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        browser.find_element(By.XPATH, '//input[@placeholder="Input first your name"]').send_keys('Manu')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('check@mail.com')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('Samib')

            # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
        time.sleep(1)

            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        text1 = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text
        text2 = "Congratulations! You have successfully registered!"

        assert text1 == text2, "Failed"

if __name__ == "__main__":
    pytest.main()

#finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
   # browser.quit()