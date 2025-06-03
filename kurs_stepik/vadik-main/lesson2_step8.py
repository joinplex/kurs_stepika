from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = 'input'
    value2 = 'lastname'
    value3 = 'email'

    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, value3)
    input3.send_keys("Smolensk@gmail.com") 

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)


    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла