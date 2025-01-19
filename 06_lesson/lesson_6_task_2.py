from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/textinput')

input_element = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input_element.send_keys('Skypro')

new_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
new_button.click()

new_button_text = new_button.text
print(new_button_text)

driver.quit()
