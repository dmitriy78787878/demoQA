# from selenium.webdriver.common.by import By

from pages.demoqa import DemoQa
# import time

def test_check_icon(browser):
# def test_icon_exist(browser):
    # browser.get("https://demoqa.com/")
    #
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')

    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    # time.sleep(3)
    # demo_qa_page.click_on_the_icon()
    demo_qa_page.icon.click()
    # time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()



