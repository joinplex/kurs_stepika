from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    #time.sleep(0.1)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #time.sleep(0.5)

    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)

    field = browser.find_element(By.TAG_NAME, "input")
    field.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
