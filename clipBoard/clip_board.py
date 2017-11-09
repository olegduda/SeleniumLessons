# -*- coding: utf-8 -*-

# Clipboard working


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from tkinter import Tk

import time

class testClipBoard(unittest.TestCase):

    TEXT_SEARCH = "Selenium and Python"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.clib_board = Tk()

    def tearDown(self):
        self.driver.quit()

    def testClipBoardAndTextArea(self):
        self.driver.get("https://clipboardjs.com/")
        self.driver.find_element_by_css_selector("button.btn[data-clipboard-action='cut']").click()
        self.driver.refresh()

        text_area = self.driver.find_element_by_id("bar").text
        text_cb = self.clib_board.clipboard_get()

        assert (text_area == text_cb)

        self.driver.get("http://google.com/")
        self.clib_board.clipboard_clear()
        self.clib_board.clipboard_append(self.TEXT_SEARCH)
        self.driver.execute_script("document.getElementById('lst-ib').focus;")

        self.driver.find_element_by_id("lst-ib").send_keys(Keys.CONTROL, 'v')
        text_area = self.driver.find_element_by_id("lst-ib").text

        print(text_area)
        print(self.TEXT_SEARCH)

        assert (self.TEXT_SEARCH == text_area)





if __name__ == "__main__":
    unittest.main()
