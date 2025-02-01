from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AuthPage import Auth
from MainPage import Main
from CartPage import Cart
from time import sleep


def test_shop_buy():
    
    test_sum = 1

    driver = webdriver.Chrome()
    auth = Auth(driver)
    auth.log_in('standard_user', 'secret_sauce')
    buy = Main(driver)
    buy.add_items_to_cart()
    check = Cart(driver)
    check.checkout('1', '1', '1')
    total_sum = check.total_sum()

    assert total_sum == test_sum
    




