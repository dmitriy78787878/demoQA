import time
from pages.text_box import TextBox

def testtextbox(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.name.send_keys('tester1')
    text_box_page.currentAddress1.send_keys('Peterburg')
    time.sleep(2)
    text_box_page.btnSubmit.click_force()

    assert text_box_page.name2.get_text() == 'Name:tester1'
    assert text_box_page.currentAddress2.get_text() == 'Current Address :Peterburg'
