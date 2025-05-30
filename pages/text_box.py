from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.currentAddress1 = WebElement(driver, '#currentAddress')
        self.btnSubmit = WebElement(driver, '#submit')
        self.name2 = WebElement(driver, '#name')
        self.currentAddress2 = WebElement(driver, '#output > div > #currentAddress')
