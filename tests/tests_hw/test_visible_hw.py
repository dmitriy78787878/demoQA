from pages.accordion import Accordion
import time

####
def test_visible_accordion(browser):
    demo_qa_page = Accordion(browser)
    demo_qa_page.visit()
    assert demo_qa_page.section1Content.visible()
    assert demo_qa_page.section1Heading.click()
    time.sleep(2)
    assert not demo_qa_page.section1Content.visible()

def test_visible_accordion_default(browser):
    demo_qa_page = Accordion(browser)
    demo_qa_page.visit()
    assert not demo_qa_page.section2Content.visible()
    assert not demo_qa_page.section2_Content.visible()
    assert not demo_qa_page.section3Content.visible()
