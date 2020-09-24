import pytest
import time
from lesson3 import locator as locator_

def find(page, locator):
    return page.find_element_by_css_selector(locator)
def find_all(page, locator):
    return page.find_elements_by_css_selector(locator)

def test_registration(browser):
        # Arrange
        browser.get(locator_.main_page)

        time.sleep(10)

        find(browser, locator_.login_link).click()

        #Act
        user_name = find(browser, locator_.registration_email_input)
        user_name.send_keys(locator_.registration_email)

        pswd1 = find(browser, locator_.registration_pswd_input1)
        pswd1.send_keys(locator_.user_pswd)

        pswd2 = find(browser, locator_.registration_pswd_input2)
        pswd2.send_keys(locator_.user_pswd)

        find(browser, locator_.registration_button).click()
        #Assert
        success_alert = find(browser, locator_.success_registration_alert).text
        assert "Спасибо за регистрацию!" in success_alert, "Profile isn't created"


