from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    elements_page = ModalDialogs(browser)
    elements_page.visit()

    assert elements_page.btnmenu.check_count_elements(count=5)

def test_navigation_modal(browser):
    elements_page = ModalDialogs(browser)
    elements_page.visit()
    browser.refresh()
    elements_page.icon1.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    elements_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)



