from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section1Content = WebElement(driver, '#section1Content > p')
        self.section1Heading = WebElement(driver, '#section1Heading')
        self.section2Content = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section2_Content = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.section3Content = WebElement(driver, '#section3Content > p')