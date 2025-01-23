from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep


username = 'standard_user'
password = 'secret_sauce'
test_sum = '$58.29'

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 5)


driver.get('https://www.saucedemo.com/')

username_input = driver.find_element(By.CSS_SELECTOR, '#user-name')
password_input = driver.find_element(By.CSS_SELECTOR, '#password')
login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

username_input.send_keys(username)
password_input.send_keys(password)
login_button.click


item_1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
item_2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
item_3 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
shopping_cart_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')

item_1.click
item_2.click
item_3.clear
shopping_cart_button.click


checkout_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')

checkout_button.click


first_name_input = driver.find_element(By.CSS_SELECTOR, '#first-name')
last_name_input = driver.find_element(By.CSS_SELECTOR, '#last-name')
postal_code_input = driver.find_element(By.CSS_SELECTOR, '#postal-code')
continue_button = driver.find_element(By.CSS_SELECTOR, '#continue')

first_name_input.send_keys('Yurii')
last_name_input.send_keys('Laz')
postal_code_input.send_keys('1234567')
continue_button.click


total_sum = driver.find_element(By.CSS_SELECTOR, '#checkout_summary_container > div > div.summary_info > div.summary_total_label').text


driver.quit()


assert total_sum == test_sum