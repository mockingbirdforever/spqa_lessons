from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 5)
delay_time = '5'


driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

delay_input = driver.find_element(By.CSS_SELECTOR, '#delay')
button_7 = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(1)')
button_8 = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(2)')
button_plus = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span:nth-child(4)')
button_equal = driver.find_element(By.CSS_SELECTOR, '#calculator > div.keys > span.btn.btn-outline-warning')
result_screen = driver.find_element(By.CSS_SELECTOR, '#calculator > div.top > div')
# думал завязаться на видимость лоадера
# spinner = driver.find_element(By.CSS_SELECTOR, '#spinner')

delay_input.clear()
delay_input.send_keys(delay_time)
button_7.click()
button_plus.click()
button_8.click()
# засекаем время перед кликом
start_time = time.time()
button_equal.click()

try:
    is_result_shown = waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15')
    )
    end_time = time.time()
except TimeoutException:
    is_result_shown = False
    end_time = time.time()

elapsed_time = end_time - start_time


# вариант с питестом не понравился
# def test_positive_result():
#     assert is_result_shown == True

assert is_result_shown == True

print(f'Но фактическое время ожидания {round(elapsed_time, 3)} сек!')

driver.quit()
