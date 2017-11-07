# -*- coding: utf-8 -*-

# basic Auth with proxy

import unittest
from selenium import webdriver
from browsermobproxy import Server

class testAuthBasic(unittest.TestCase):

    def setUp(self):
        self.server = Server(r"C:\Users\user\Documents\ScrinShots\SeleniumLessons\basic_auth\browsermob-proxy\bin\browsermob-proxy")
        self.server.start()

        self.proxy = self.server.create_proxy()

        self.profile = webdriver.FirefoxProfile()

        self.profile.set_proxy(self.proxy.selenium_proxy())

        self.driver = webdriver.Firefox(firefox_profile=self.profile)
        self.driver.implicitly_wait(8)

        self.driver.get("https://auth-demo.aerobatic.io/")


    def tearDown(self):
        self.server.stop()
        self.driver.quit()

    def test_search(self):

        self.proxy.basic_authentication("auth-demo.aerobatic.io","aerobatic","aerobatic")
        self.driver.get("https://auth-demo.aerobatic.io/protected-standard/")

        assert self.driver.find_element_by_css_selector("a.button-primary[href='/']")


if __name__ == "__main__":
    unittest.main()
