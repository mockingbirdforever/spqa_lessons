from selenium import webdriver
from time import sleep
import random

driver = webdriver.Chrome()

randon_number = random.randint(0, 1000)
screenshot_name = f'ya{randon_number}.png'

driver.get("https://ya.ru/")
sleep(2)

driver.fullscreen_window()
sleep(2)


driver.save_screenshot(screenshot_name)

