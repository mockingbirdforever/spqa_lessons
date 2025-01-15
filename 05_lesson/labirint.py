from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from prettytable import PrettyTable


driver = webdriver.Chrome()
table = PrettyTable()
table.field_names = ['Название', 'Автор', 'Текущая цена', 'Цена без скидки']
table.align['Название'] = 'l'
table.align['Автор'] = 'l'
table.sortby = "Текущая цена"

driver.get("https://www.labirint.ru/")
search_input = driver.find_element(By.CSS_SELECTOR, '#search-field')
search_input.send_keys("Computer vision")
search_input.send_keys(Keys.RETURN)

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

for book in books:

    name = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text

    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except BaseException:
        author = 'Имярек'

    try:
        current_price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
        current_price = int(current_price[:-2].replace(' ', ''))
    except BaseException:
        current_price = '??'

    try:
        old_price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-val-old.tooltip').text
    except BaseException:
        old_price = '??'

    # print(f'"{name}". {author} - {current_price} ({old_price})')
    table.add_row([name, author, current_price, old_price])

print(table)
