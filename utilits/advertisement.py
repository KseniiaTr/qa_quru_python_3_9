from selene import command, have
from selene.support.shared import browser


def remove_ads(selector):
    browser.all(selector).with_(timeout=5).wait_until(have.size_greater_than_or_equal(3))
    browser.all(selector).perform(command.js.remove)