# -*- coding: utf-8 -*-

# Tabs and windows goto

import unittest

from selenium import webdriver

from .utils.auth_login import *
from .pages.multi_pages import *


class testSubmenuOpen(unittest.TestCase):

    __page_load_start = "http://way2automation.com/way2auto_jquery/index.php"
    __page_load = "http://way2automation.com/way2auto_jquery/frames-and-windows.php"
    __name_link_tab = "Open Window-1"

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

        page = MultiPages(self.driver)
        page.clic_open_omp()
        page.switch_to_frame()
        page.click_link()
        page.goto_new_tab()
        page.click_link()

        self.assertTrue(page.goto_new_tab_text(self.__name_link_tab), "windows level three not open")


if __name__ == "__main__":
    unittest.main()
