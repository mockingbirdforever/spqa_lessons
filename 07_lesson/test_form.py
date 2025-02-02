from selenium import webdriver
from lesson_7_task_1.DataTypesFormPage import FormPage
from lesson_7_task_1.DataTypesFilledFormPage import FilledFormPage
from lesson_7_task_1.configurator import *


def test_form():
    driver = webdriver.Chrome()

    form = FormPage(driver)

    form.fill_first_name(first_name)
    form.fill_last_name(last_name)
    form.fill_address(address)
    form.fill_zip_code(zip_code)
    form.fill_city(city)
    form.fill_country(country)
    form.fill_email(email)
    form.fill_phone(phone)
    form.fill_job_position(job_position)
    form.fill_company(company)
    form.click_submit_button()

    filled = FilledFormPage(driver)

    assert filled.check_first_name(first_name) is True
    assert filled.check_last_name(last_name) is True
    assert filled.check_address(address) is True
    assert filled.check_zip_code(zip_code) is False  # негативная проверка
    assert filled.check_city(city) is True
    assert filled.check_country(country) is True
    assert filled.check_email(email) is True
    assert filled.check_phone(phone) is True
    assert filled.check_job_position(job_position) is True
    assert filled.check_company(company) is True

    driver.quit()




