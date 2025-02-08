from selenium import webdriver
from lesson_7_task_2.Calculator import Calculator


def test_calculator():
    delay = 5
    num1 = 3
    num2 = 6
    expected_result = num1 + num2

    driver = webdriver.Chrome()

    calc = Calculator(driver)
    calc.set_delay(delay)
    calc.sum_function(num1, num2)
    actual_result = calc.check_result(expected_result, delay)

    driver.quit()

    assert expected_result == actual_result
