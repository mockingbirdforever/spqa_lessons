from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_first_name(self, first_name):
        self._driver.find_element(By.NAME, 'first-name').send_keys(first_name)

    def fill_last_name(self, last_name):
        self._driver.find_element(By.NAME, 'last-name').send_keys(last_name)

    def fill_address(self, address):
        self._driver.find_element(By.NAME, 'address').send_keys(address)

    def fill_zip_code(self, zip_code):
        self._driver.find_element(By.NAME, 'zip-code').send_keys(zip_code)

    def fill_city(self, city):
        self._driver.find_element(By.NAME, 'city').send_keys(city)

    def fill_country(self, country):
        self._driver.find_element(By.NAME, 'country').send_keys(country)

    def fill_email(self, email):
        self._driver.find_element(By.NAME, 'e-mail').send_keys(email)

    def fill_phone(self, phone):
        self._driver.find_element(By.NAME, 'phone').send_keys(phone)

    def fill_job_position(self, job_position):
        self._driver.find_element(By.NAME, 'job-position').send_keys(job_position)

    def fill_company(self, company):
        self._driver.find_element(By.NAME, 'company').send_keys(company)

    def click_submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

