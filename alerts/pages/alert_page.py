# -*- coding: utf-8 -*-

# multi pages way

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import *


class AlertPages(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_wite = WebDriverWait(self.driver, 10)
        self.loc = AlertLocators()

    def click_batton_frame(self):
        self.driver_wite.until(EC.element_to_be_clickable(self.loc.IFRAME_BUTTON)).click()

    def switch_to_frame(self):
        self.driver_wite.until(EC.frame_to_be_available_and_switch_to_it(self.loc.IFRAME_ALERT))

    def click_input_alert(self):
        self.driver_wite.until(EC.element_to_be_clickable(self.loc.INPUT_ALERT)).click()

    def get_frame_text(self):
        return self.driver_wite.until(EC.element_to_be_clickable(self.loc.IFRAME_TEXT)).text

    def get_link_text(self):
        self.text = self.driver_wite.until(EC.element_to_be_clickable(self.loc.LINK_NEW_TAB)).text
        return str(self.text)


class AlertModalWindows():

    def __init__(self, driver):
        self.driver = driver
        self.alert = self.driver.switch_to_alert()

    def set_text_and_close(self, text):
        self.alert.send_keys(text)
        self.alert.accept()



