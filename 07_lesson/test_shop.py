from selenium import webdriver
from lesson_7_task_3.AuthPage import Auth
from lesson_7_task_3.MainPage import Main
from lesson_7_task_3.CartPage import Cart


def test_shop_buy():
    
    test_sum = 'Total: $58.29'

    driver = webdriver.Chrome()
    auth = Auth(driver)
    auth.log_in('standard_user', 'secret_sauce')
    buy = Main(driver)
    buy.add_items_to_cart()
    check = Cart(driver)
    check.checkout('Yuri', 'Laz', '123456')
    total_sum = check.total_sum()

    driver.quit()

    assert total_sum == test_sum


    




