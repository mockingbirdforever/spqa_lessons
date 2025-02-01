from selenium import webdriver
from selenium.webdriver.common.by import By
from configurator import *


def test_shop_buy():
    driver = webdriver.Chrome()

    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(customer_first_name)
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(customer_last_name)
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(customer_postal_code)
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    total_sum = driver.find_element(By.CSS_SELECTOR, '[data-test=total-label]').text

    driver.quit()

    assert total_sum == test_sum
