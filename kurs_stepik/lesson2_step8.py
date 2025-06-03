from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    # Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Иван")
    browser.find_element(By.NAME, "lastname").send_keys("Петров")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    
    # Создаем временный файл для загрузки
    with open("test_file.txt", "w") as file:
        file.write("This is a test file")  # Можно оставить пустым
    
    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    
    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # Даем время скопировать код и удаляем временный файл
    time.sleep(10)
    browser.quit()
    if os.path.exists("test_file.txt"):
        os.remove("test_file.txt")