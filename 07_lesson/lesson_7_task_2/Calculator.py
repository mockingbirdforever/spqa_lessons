from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    def set_delay(self, seconds):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(seconds)

    def sum_function(self, num1, num2):
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def sub_function(self, num1, num2):
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'-')]").click()
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def mul_function(self, num1, num2):
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'x')]").click()
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def div_function(self, num1, num2):
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'÷')]").click()
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

    def check_result(self, expected_result, delay):
        waiter = WebDriverWait(self._driver, delay + 1)
        waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), str(expected_result))
        )
        actual_result = self._driver.find_element(By.CSS_SELECTOR, "div[class='screen']").get_attribute("innerText")
        return int(actual_result)



