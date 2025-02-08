from selenium.webdriver.common.by import By


class FilledFormPage:

    def __init__(self, driver):
        self._driver = driver

    def check_first_name(self, first_name):
        return first_name == self._driver.find_element(
            By.ID, 'first-name').text

    def check_last_name(self, last_name):
        return last_name == self._driver.find_element(By.ID, 'last-name').text

    def check_address(self, address):
        return address == self._driver.find_element(By.ID, 'address').text

    def check_zip_code(self, zip_code):
        return zip_code == self._driver.find_element(By.ID, 'zip-code').text

    def check_city(self, city):
        return city == self._driver.find_element(By.ID, 'city').text

    def check_country(self, country):
        return country == self._driver.find_element(By.ID, 'country').text

    def check_email(self, email):
        return email == self._driver.find_element(By.ID, 'e-mail').text

    def check_phone(self, phone):
        return phone == self._driver.find_element(By.ID, 'phone').text

    def check_job_position(self, job_position):
        return job_position == self._driver.find_element(
            By.ID, 'job-position').text

    def check_company(self, company):
        return company == self._driver.find_element(By.ID, 'company').text
