from selene import have


class Radiobutton:
    def __init__(self, element):
        self.element = element

    def choose_gender(self, value):
        self.element.element_by(have.value(value)).element('..').click()
