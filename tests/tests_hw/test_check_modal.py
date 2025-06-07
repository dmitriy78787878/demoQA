import time

from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    page_browser = ModalDialogs(browser)
    page_browser.visit()
    page_browser.btnSmallModal.click()
    time.sleep(2)
    assert page_browser.SmallModal.exist()
    page_browser.btnCloseSmallModal.click()
    assert not page_browser.SmallModal.exist()

    page_browser.btnLargeModal.click()
    time.sleep(2)
    assert page_browser.LargeModal.exist()
    page_browser.btnCloseLargeModal.click()
    assert not page_browser.LargeModal.exist()

