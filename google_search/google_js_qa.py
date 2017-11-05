# -*- coding: utf-8 -*-

# google search

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class testGoogleSearch(unittest.TestCase):

    PAGE_LOAD = "http://google.com/"

    def wait_for_page_to_load(self, timeout=10000):
        w = WebDriverWait(self.driver, timeout / 100.0)
        w.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(18)
        self.driver.get(self.PAGE_LOAD)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        # Width of the search field
        input_width = self.driver.execute_script("return document.getElementById('lst-ib').offsetWidth;")

        # Is a scrolling page
        is_scroll_page = self.driver.execute_script("return document.body.clientHeight-document.documentElement.clientHeight;")

        # Enter the query
        input_str_search = self.driver.execute_script("document.getElementById('lst-ib').value='Selenium';")

        # Take off focus
        input_str_search = self.driver.execute_script("document.getElementById('lst-ib').blur;")

        # Perform a search
        input_str_search = self.driver.execute_script("document.getElementById('_fZl').click();")

        # Verifying page loading
        WebDriverWait(self.driver, 8).until(lambda driver: self.driver.execute_script("return document.getElementById('navcnt');"))

        is_scroll_page = self.driver.execute_script("return document.body.clientHeight-document.documentElement.clientHeight;")



if __name__ == "__main__":
    unittest.main()

'''
function get_scroll(a) {
   var d = document,
        b = d.body,
        e = d.documentElement,
        c = "client" + a;
        a = "scroll" + a;
   return /CSS/.test(d.compatMode)? (e[c]< e[a]) : (b[c]< b[a])
};
get_scroll('Height')
'''


