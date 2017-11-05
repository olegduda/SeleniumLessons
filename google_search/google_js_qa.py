# -*- coding: utf-8 -*-

# google search

import unittest

from .google_pages import *

class testGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.home_page.open()
        self.home_page.width_input_field()
        self.home_page.is_scloll_page()
        self.home_page.input_text()
        self.home_page.off_focus()
        self.home_page.click_page()

        assert (self.home_page.verify_load_page()), "Page not load"
        assert (self.home_page.is_scloll_page()), "Page not scroll"

if __name__ == "__main__":
    unittest.main()


