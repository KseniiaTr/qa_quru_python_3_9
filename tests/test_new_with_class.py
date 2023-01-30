from selene.support.shared import browser

from model.data.User import User
from pages import new_practice_form
from pages.new_practice_form import PracticeForm


def test_submit_filled_form():
    browser.open('https://demoqa.com/automation-practice-form')

    new_practice_form.hide_adv()

    user = User(first_name='Alex',
                last_name='Alekseev',
                email='alexalekseev@gmail.com',
                phone='8910123121',
                gender='Male',
                birthday_month='May',
                birthday_year='1991',
                birthday_day='7',
                subject='History',
                hobby='Music',
                photo='Photo_test_yellow.png',
                adress='Delhi, Pyatnitskaya st 12/12',
                state='NCR',
                city='Delhi')

    practice_form = PracticeForm()
    practice_form.fill_data(user).submit()
    practice_form.should_have_registered(user)
