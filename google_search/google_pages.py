# -*- coding: utf-8 -*-

# google pages

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

PAGE_LOAD = "http://google.com/"
TEXT_SEARCH = "Selenium and Python"

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(16)

    def open(self, page_load=PAGE_LOAD):
        self.driver.get(page_load)
        return self

    def width_input_field(self):
        input_width = self.driver.execute_script("return document.getElementById('lst-ib').offsetWidth;")
        return input_width

    def is_scloll_page(self):
        is_scroll = self.driver.execute_script("return document.body.clientHeight-document.documentElement.clientHeight;")
        if is_scroll == 0:
            is_scroll = False
        else:
            is_scroll = True
        return is_scroll

    def input_text(self,text_search=TEXT_SEARCH):
        self.driver.execute_script("document.getElementById('lst-ib').value='" + text_search +"';")

    def off_focus(self):
        self.driver.execute_script("document.getElementById('lst-ib').blur;")

    def verify_load_page(self):
        try:
            WebDriverWait(self.driver, 8).until(
                lambda driver: self.driver.execute_script("return document.getElementById('navcnt');"))
            is_load = True
        except:
            is_load = False
        return is_load

    def click_page(self):
        self.driver.execute_script("document.getElementById('_fZl').click();")

