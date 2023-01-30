from selene import have
from selene.support.shared import browser


class Checkbox:
    def __init__(self, element):
        self.element = element

    def choose_hobbies(self, text):
        self.element.should(have.exact_text(text)).click()
