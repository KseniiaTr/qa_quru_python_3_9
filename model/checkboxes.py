from selene import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def choose_hobbies(self, text):
        self.element.should(have.exact_text(text)).click()
