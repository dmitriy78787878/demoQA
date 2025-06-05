from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        #self.btn_delete_row = WebElement(driver, '#delete-record-1 > svg > path')
        self.btnAdd = WebElement(driver, '#addNewRecordButton')
        self.FirstName = WebElement(driver, '#firstName')
        self.LastName = WebElement(driver, '#lastName')
        self.Email = WebElement(driver, '#userEmail')
        self.Age = WebElement(driver, '#age')
        self.Salary = WebElement(driver, '#salary')
        self.Departament = WebElement(driver, '#department')
        self.Submit = WebElement(driver, '#submit')
        self.novalidate = WebElement(driver, '#userForm')
        self.SearchBox = WebElement(driver, '#searchBox')

        self.tableFirstName = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.tableLastName = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(2)')
        self.tableAge = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(3)')
        self.tableEmail = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(4)')
        self.tableSalary = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(5)')
        self.tableDepartament = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(6)')
        self.redactir = WebElement(driver, '#edit-record-4')
        self.btnDelete = WebElement(driver, '#delete-record-4')


