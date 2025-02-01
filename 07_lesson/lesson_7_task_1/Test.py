from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from DataTypesMainPage import MainPage

driver = webdriver.Chrome()

main_page = MainPage(driver)

main_page.fill_first_name('Ализмат')
main_page.click_submit_button()
sleep(5)

driver.quit()

