# -*- coding: utf-8 -*-

# Alert input text

import unittest

from selenium import webdriver

from .utils.auth_login import *
from .pages.alert_page import *


class testSubmenuOpen(unittest.TestCase):

    __page_load_start = "http://way2automation.com/way2auto_jquery/index.php"
    __page_load = "http://way2automation.com/way2auto_jquery/alert.php"
    __alert_text = "Selenium user"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.driver.get(self.__page_load_start)
        self.driver_wait = WebDriverWait(self.driver, 10)
        authSite().auth_login(self.driver, self.driver_wait)
        self.driver.get(self.__page_load)

    def tearDown(self):
        self.driver.quit()

    def testMultiTabs(self):

        page = AlertPages(self.driver)
        page.click_input_alert()
        page.switch_to_frame()
        page.click_batton_frame()

        alert = AlertModalWindows(self.driver)
        alert.set_text_and_close(self.__alert_text)

        frame_text_alert = page.get_frame_text()
        frame_text_alert.find(self.__alert_text)

        self.assertTrue(frame_text_alert.find(self.__alert_text), "text not change")


if __name__ == "__main__":
    unittest.main()
