# -*- coding: utf-8 -*-

# google search

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        is_scroll = '''return function get_scroll(a){var d = document, b = d.body, e = d.documentElement, c = "client" + a; a = "scroll" + a;return /CSS/.test(d.compatMode)? (e[c]< e[a]) : (b[c]< b[a]) }; get_scroll('Height');'''

        input_width = self.driver.execute_script("return document.getElementById('lst-ib').offsetWidth;")
        print(input_width)

        is_scroll_page = self.driver.execute_script(is_scroll)
        print(is_scroll_page)

        is_scroll_page = self.driver.execute_script("return document.documentElement.scrollHeight == document.documentElement.offsetHeight;")
        print(is_scroll_page)

        input_str_search = self.driver.execute_script("document.getElementById('lst-ib').value='Selenium';")
        input_str_search = self.driver.execute_script("document.getElementById('lst-ib').blur;")

        input_str_search = self.driver.execute_script("document.getElementById('_fZl').click();")
        is_load = input_str_search = self.driver.execute_script("return document.body.onload;")
        print(is_load)

        self.driver.execute_script("return (typeof MathJax === 'undefined') || (MathJax.Hub.signal.posted[window.MathJax.Hub.signal.posted.length-1][0]=='End Process')")

        self.wait_for_page_to_load()

        is_scroll_page = self.driver.execute_script("return document.documentElement.scrollHeight == document.documentElement.offsetHeight;")
        print(is_scroll_page)


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


