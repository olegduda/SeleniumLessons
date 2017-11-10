# -*- coding: utf-8 -*-

# Clipboard working


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import Tk

import pyperclip


PAGE_CBJS = "https://clipboardjs.com/"
PAGE_GOOGLE = "http://google.com/"
TEXT_SEARCH = "Selenium and Python"
INPUT_ID_GL = "lst-ib"

class testClipBoard(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.clib_board = Tk()

    def tearDown(self):
        self.driver.quit()

    def testClipBoardAndTextArea(self):
        self.driver.get(PAGE_CBJS)
        self.driver.find_element_by_css_selector("button.btn[data-clipboard-action='cut']").click()
        self.driver.refresh()

        text_area = self.driver.find_element_by_id("bar").get_attribute("value")
        text_cb = self.clib_board.clipboard_get()

        assert (text_area == text_cb)

    def testClipBoardSetText(self):
        self.driver.get(PAGE_GOOGLE)

        pyperclip.copy(TEXT_SEARCH)
        self.driver.find_element_by_id(INPUT_ID_GL).click()

        self.driver.find_element_by_id(INPUT_ID_GL).send_keys(Keys.CONTROL, 'v')
        text_area = self.driver.find_element_by_id(INPUT_ID_GL).get_attribute("value")

        assert (TEXT_SEARCH == text_area)


if __name__ == "__main__":
    unittest.main()
