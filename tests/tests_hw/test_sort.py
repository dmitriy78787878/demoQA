from pages.tables import Tables
import time

def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.HtableFirstName.click()
    time.sleep(2)
    assert page_tables.HtableFirstName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.HtableLastName.click()
    time.sleep(2)
    assert page_tables.HtableLastName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.HtableAge.click()
    time.sleep(2)
    assert page_tables.HtableAge.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.HtableEmail.click()
    time.sleep(2)
    assert page_tables.HtableEmail.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.HtableSalary.click()
    time.sleep(2)
    assert page_tables.HtableSalary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    page_tables.HtableDepartament.click()
    time.sleep(2)
    assert page_tables.HtableDepartament.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
