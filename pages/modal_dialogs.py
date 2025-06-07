from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btnmenu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon1 = WebElement(driver, '#app > header > a')
        self.btnSmallModal = WebElement(driver, '#showSmallModal')
        self.btnLargeModal = WebElement(driver, '#showLargeModal')
        self.SmallModal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btnCloseSmallModal = WebElement(driver, '#closeSmallModal')
        self.LargeModal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.btnCloseLargeModal = WebElement(driver, '#closeLargeModal')