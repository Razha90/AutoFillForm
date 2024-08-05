from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import random
import time

form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScnHY36UfTz3gsS7CJfGYRYyzCkoO7BX7IdEZza6KfoVWN7ZQ/viewform'


driver = webdriver.Chrome()

try:
    driver.get(form_url)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'Qr7Oae'))
    )

    questions = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')

    for question in questions:
        try:
            choices = question.find_elements(By.XPATH, './/div[@role="radio"]')
            if choices:
                weights = [0.1, 0.1, 0.3, 0.3, 0.2]
                random_choice = random.choices(choices, weights)[0]
                driver.execute_script("arguments[0].scrollIntoView();", random_choice)
                random_choice.click()
                time.sleep(1)

        except Exception as e:
            print(f"Error saat memilih radio button: {e}")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @aria-label="Submit"]'))
    )
    submit_button.click()


    time.sleep(5)

finally:
    driver.quit()