from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def test_calculator():

    driver = webdriver.Chrome()
    waiter = WebDriverWait(driver, 5)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys('5')
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)').click()  # 7
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)').click()  # +
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)').click()  # 8
    driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning').click()  # =

    try:
        is_result_shown = waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15')
        )
    except TimeoutException:
        is_result_shown = False

    assert is_result_shown is True

    driver.quit()
