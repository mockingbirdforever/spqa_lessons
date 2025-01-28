from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from configurator import *


driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


driver.find_element(By.NAME, 'first-name').send_keys(text_first_name)
driver.find_element(By.NAME, 'last-name').send_keys(text_last_name)
driver.find_element(By.NAME, 'address').send_keys(text_address)
driver.find_element(By.NAME, 'zip-code').send_keys(text_zip_code)
driver.find_element(By.NAME, 'city').send_keys(text_city)
driver.find_element(By.NAME, 'country').send_keys(text_country)
driver.find_element(By.NAME, 'e-mail').send_keys(text_email)
driver.find_element(By.NAME, 'phone').send_keys(text_phone)
driver.find_element(By.NAME, 'job-position').send_keys(text_job_position)
driver.find_element(By.NAME, 'company').send_keys(text_company)

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


@pytest.mark.parametrize('text, text_filled', [
    (text_first_name, driver.find_element(By.ID, 'first-name').text),
    (text_last_name, driver.find_element(By.ID, 'last-name').text),
    (text_address, driver.find_element(By.ID, 'address').text),
    (text_city, driver.find_element(By.ID, 'city').text),
    (text_country, driver.find_element(By.ID, 'country').text),
    (text_email, driver.find_element(By.ID, 'e-mail').text),
    (text_phone, driver.find_element(By.ID, 'phone').text),
    (text_job_position, driver.find_element(By.ID, 'job-position').text),
    (text_company, driver.find_element(By.ID, 'company').text),
])
def test_positive_input(text, text_filled):
    assert text == text_filled


@pytest.mark.parametrize('text', [
    driver.find_element(By.ID, 'zip-code').text
])
def test_negative_input(text):
    assert text == text_n_a


driver.quit()
