from selene import command, have
from selene.support.shared import browser

from model.checkboxes import Checkbox
from model.data.User import User
from model.datapicker_class import Datepicker
from model.dropdown import Dropdown
from model.radiobutton import Radiobutton
from utilits import advertisement
from utilits.upload_image import Image


def hide_adv():
    advertisement.remove_ads('[id^=google_ads][id$=container__]')


class PracticeForm:
    def fill_data(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)

        gender = Radiobutton(browser.all('[name=gender]'))
        gender.choose_gender(user.gender)

        browser.element('#userNumber').type(user.phone)

        birthday = Datepicker(browser.element('#dateOfBirthInput'))
        birthday.set_date(user.birthday_month, user.birthday_year, user.birthday_day)

        browser.element('#subjectsInput').type(user.subject).press_enter()

        hobby = Checkbox(browser.element('[type=checkbox][id=hobbies-checkbox-3]+label'))
        hobby.choose_hobbies(user.hobby)

        path = Image(browser.element('#uploadPicture'))
        path.add_image(user.photo)

        browser.element('#currentAddress').perform(command.js.set_value(user.adress))

        state = Dropdown(browser.element('#react-select-3-input'))
        state.dropdown_state(user.state)

        city = Dropdown(browser.element('#react-select-4-input'))
        city.dropdown_city(user.city)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_registered(self, user: User):
        browser.all('.table-responsive td:nth-child(2)').should(have.texts
                                                                (user.first_name + ' ' + user.last_name,
                                                                 user.email,
                                                                 user.gender,
                                                                 user.phone,
                                                                 user.birthday_day + ' ' + user.birthday_month + ',' +
                                                                 user.birthday_year,
                                                                 user.subject,
                                                                 user.hobby,
                                                                 user.photo,
                                                                 user.adress,
                                                                 user.state + ' ' + user.city))
        return self












