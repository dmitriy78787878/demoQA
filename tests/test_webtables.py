# import allure
# page_tables.visit()
# assert not page_tables.no_data.exist()
#
# while page_tables.btn_delete_row.exist():
#     page_tables.btn_delete_row.click()
#
# time.sleep(2)
# assert page_tables.no_data.exist()

# ДЗ 11
from pages.tables import Tables
import time

def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    page_tables.btnAdd.click()
    page_tables.FirstName.send_keys('')
    page_tables.LastName.send_keys('')
    page_tables.Email.send_keys('')
    page_tables.Age.send_keys('')
    page_tables.Salary.send_keys('')
    page_tables.Departament.send_keys('')
    page_tables.Submit.click()
    assert page_tables.novalidate.get_dom_attribute('class') == 'was-validated'

    page_tables.visit()
    page_tables.btnAdd.click()
    page_tables.FirstName.send_keys('tester')
    page_tables.LastName.send_keys('test')
    page_tables.Email.send_keys('123t@tt.ru')
    page_tables.Age.send_keys('50')
    page_tables.Salary.send_keys('111')
    page_tables.Departament.send_keys('222')
    time.sleep(2)
    page_tables.Submit.click_force()
    time.sleep(2)
    assert not page_tables.novalidate.exist()

    page_tables.SearchBox.send_keys('tester')
    time.sleep(2)
    assert page_tables.tableFirstName.get_text() == 'tester'
    assert page_tables.tableLastName.get_text() == 'test'
    assert page_tables.tableEmail.get_text() == '123t@tt.ru'
    assert page_tables.tableAge.get_text() == '50'
    assert page_tables.tableSalary.get_text() == '111'
    assert page_tables.tableDepartament.get_text() == '222'
    page_tables.redactir.click()
    assert page_tables.novalidate.exist()
    page_tables.FirstName.clear()
    time.sleep(2)
    page_tables.FirstName.send_keys('My name')
    page_tables.Submit.click()
    time.sleep(2)
    page_tables.SearchBox.clear()
    time.sleep(2)
    page_tables.SearchBox.send_keys('My name')
    time.sleep(2)
    assert page_tables.tableFirstName.get_text() == 'My name'
    page_tables.btnDelete.click()
    page_tables.SearchBox.clear()
    page_tables.SearchBox.send_keys('My name')
    time.sleep(2)
    assert page_tables.tableFirstName.get_text() == ' '
    assert page_tables.tableLastName.get_text() == ' '
    assert page_tables.tableEmail.get_text() == ' '
    assert page_tables.tableAge.get_text() == ' '
    assert page_tables.tableSalary.get_text() == ' '
    assert page_tables.tableDepartament.get_text() == ' '





