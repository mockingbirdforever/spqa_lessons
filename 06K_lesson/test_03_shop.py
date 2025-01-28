from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from configurator import *


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 5)


driver.get('https://www.saucedemo.com/')

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '#login-button').click()


item_1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
item_2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
item_3 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
shopping_cart_button = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')

item_1.click()
item_2.click()
item_3.click()
shopping_cart_button.click()


driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(customer_first_name)
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(customer_last_name)
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(customer_postal_code)
driver.find_element(By.CSS_SELECTOR, '#continue').click()



total_sum = driver.find_element(By.CSS_SELECTOR, '#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
total_sum = total_sum[7:]


driver.quit()

print(total_sum)

assert total_sum == test_sum
