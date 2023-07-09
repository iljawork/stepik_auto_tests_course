from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(y)
    checbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()