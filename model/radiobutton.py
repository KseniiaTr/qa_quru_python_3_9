from selene import have
from selene.support.shared import browser


class Radiobutton:
    def __init__(self, element):
        self.element = element

    def choose_gender(self, value):
        self.element.element_by(have.value(value)).element('..').click()
