from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    def calc(x):
        return str(int(x) + int(z))

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = x_element.text
    z_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    z = z_element.text
    y = calc(x)

    browser.find_element(By.ID, "dropdown").click()
    time.sleep(1)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()