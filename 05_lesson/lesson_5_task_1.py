# Задание 3. Клик по кнопке

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
button = driver.find_element(By.CSS_SELECTOR, 'button')

for i in range(0, 5):
    button.click()

delete_button = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')

print(len(delete_button))

driver.quit()

# предыдущий вариант
# delete_buttons = []
#
# for i in range(0, 5):
#     button.click()
#     delete_button = driver.find_element(By.CSS_SELECTOR, 'button.added-manually').text
#     delete_buttons.append(delete_button)
#
# print(len(delete_buttons))
