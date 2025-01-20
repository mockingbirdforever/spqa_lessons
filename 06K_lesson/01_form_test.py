from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions as EC

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

first_name.send_keys('Иван')
last_name.send_keys('Петров')
address.send_keys('Ленина, 55-3')
# zip_code.send_keys('')
city.send_keys('Москва')
country.send_keys('Россия')
email.send_keys('test@skypro.com')
phone.send_keys('+7985899998787')
job_position.send_keys('QA')
company.send_keys('SkyPro')

submit_button.click()

city = "//*[@id='city']"

element1 = driver.find_element(By.XPATH, city).text


@pytest.mark.parametrize('locator, result', [
    ("//*[@id='city']", 'Москва'),
])
def positive_parameters(locator, result):
    locator_text = driver.find_element(By.XPATH, locator).text
    assert locator_text == result


driver.quit()
