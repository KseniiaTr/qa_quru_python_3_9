import os
from importlib import resources

from selene.support.shared import browser

import tests


class Image:
    def __init__(self, element):
        self.element = element

    def add_image(self, path):
        main_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests/resources')
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(main_path, path)
            )
        )

