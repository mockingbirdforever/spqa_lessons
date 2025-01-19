from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()


driver.get("http://ya.ru/")
sleep(2)

current = driver.current_url

driver.quit()


print(current[:5])
