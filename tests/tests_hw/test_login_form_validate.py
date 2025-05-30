from pages.form_page import FormPage
import time
def test_login_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.first_name.send_keys('')
    form_page.last_name.send_keys('')
    form_page.user_email.send_keys('')
    form_page.user_number.send_keys('')
    form_page.current_address.send_keys('')
    time.sleep(2)
    form_page.btn_submit.click_force()

    assert form_page.novalidate.get_dom_attribute('class') == 'was-validated'
