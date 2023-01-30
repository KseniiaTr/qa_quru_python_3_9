from selene.support.shared import browser


class Dropdown:
    def __init__(self, element):
        self.element = element

    def dropdown_state(self, value):
        self.element.send_keys(value).press_enter()

    def dropdown_city(self, value):
        self.element.send_keys(value).press_enter()


