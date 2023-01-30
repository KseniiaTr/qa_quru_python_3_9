
from selene.support.shared import browser


class Datepicker:
    def __init__(self, element):
        self.element = element

    def set_date(self, month, year, day):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--00{day}').click()


