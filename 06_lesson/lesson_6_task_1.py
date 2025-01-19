from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 20)

driver.get('http://uitestingplayground.com/ajax')

driver.find_element(By.ID, 'ajaxButton').click()

text = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
).text

print(text)
driver.quit()
