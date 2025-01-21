from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

text_first_name = 'Иван'
text_last_name = 'Петров'
text_address = 'Ленина, 55-3'
text_zip_code = ''
text_city = 'Москва'
text_country = 'Россия'
text_email = 'test@skypro.com'
text_phone = '+7985899998787'
text_job_position = 'QA'
text_company = 'SkyPro'
text_n_a = 'N/A'


driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[1]/label/input')
last_name = driver.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[2]/label/input')
address = driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[1]/label/input')
zip_code = driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[2]/label/input')
city = driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[3]/label/input')
country = driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[4]/label/input')
email = driver.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[1]/label/input')
phone = driver.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[2]/label/input')
job_position = driver.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[1]/label/input')
company = driver.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[2]/label/input')
submit_button = driver.find_element(By.XPATH, '/html/body/main/div/form/div[5]/div/button')

first_name.send_keys(text_first_name)
last_name.send_keys(text_last_name)
address.send_keys(text_address)
# не отправляем для проверки негативного кейса
# zip_code.send_keys(text_zip_code)
city.send_keys(text_city)
country.send_keys(text_country)
email.send_keys(text_email)
phone.send_keys(text_phone)
job_position.send_keys(text_job_position)
company.send_keys(text_company)

submit_button.click()


first_name_filled = driver.find_element(By.XPATH, '//*[@id="first-name"]').text
last_name_filled = driver.find_element(By.XPATH, '//*[@id="last-name"]').text
address_filled = driver.find_element(By.XPATH, '//*[@id="address"]').text
zip_code_filled = driver.find_element(By.XPATH, '//*[@id="zip-code"]').text
city_filled = driver.find_element(By.XPATH, '//*[@id="city"]').text
country_filled = driver.find_element(By.XPATH, '//*[@id="country"]').text
email_filled = driver.find_element(By.XPATH, '//*[@id="e-mail"]').text
phone_filled = driver.find_element(By.XPATH, '//*[@id="phone"]').text
job_position_filled = driver.find_element(By.XPATH, '//*[@id="job-position"]').text
company_filled = driver.find_element(By.XPATH, '//*[@id="company"]').text


@pytest.mark.parametrize('text, text_filled', [
    (text_first_name, first_name_filled),
    (text_last_name, last_name_filled),
    (text_address, address_filled),
    (text_city, city_filled),
    (text_country, country_filled),
    (text_email, email_filled),
    (text_phone, phone_filled),
    (text_job_position, job_position_filled),
    (text_company, company_filled),
])
def test_positive_input(text, text_filled):
    assert text == text_filled


@pytest.mark.parametrize('text', [
    zip_code_filled
])
def test_negative_input(text):
    assert text == text_n_a


driver.quit()
