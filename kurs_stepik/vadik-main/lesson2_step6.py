from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    y_elem = browser.find_element(By.CSS_SELECTOR, 'input#answer.form-control')
    y_elem.send_keys(y)

    checkbox_elem = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox_elem.click()

    radiobutton_elem = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radiobutton_elem.click()

    # Отправляем заполненную форму
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()