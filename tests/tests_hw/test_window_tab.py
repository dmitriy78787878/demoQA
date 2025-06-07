import time

from pages.demoqa_links import Links

def test_check_demoqa_links(browser):
    page_link = Links(browser)
    page_link.visit()
    page_link.linkHome.exist()
    assert page_link.linkHome.get_dom_attribute('href') == 'https://demoqa.com'
    assert page_link.linkHome.get_text() == 'Home'

    assert len(browser.window_handles) == 1
    page_link.linkHome.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2




