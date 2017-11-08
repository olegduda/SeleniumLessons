# -*- coding: utf-8 -*-

# basic Auth

import unittest
from selenium import webdriver
from browsermobproxy import Server, Client
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By

import time

import requests

class testAuthBasic(unittest.TestCase):

    def setUp(self):
        self.server = Server("browsermob-proxy/bin/browsermob-proxy")
        self.server.start()
        self.proxy = self.server.create_proxy()

        self.profile = webdriver.FirefoxProfile()

        self.profile.set_proxy(self.proxy.selenium_proxy())
        #self.driver.capabilities
        self.driver = webdriver.Firefox(firefox_profile=self.profile)
        self.driver.implicitly_wait(8)



        self.proxy.new_har("aerobatic")
        self.driver.get("https://auth-demo.aerobatic.io/")


    def tearDown(self):
        self.server.stop()
        self.driver.quit()

    def test_search(self):
        print(self.proxy.har)


        self.driver.find_element_by_css_selector("a.button-primary[href='/protected-standard/']").click()
        self.proxy.basic_authentication("auth-demo.aerobatic.io","aerobatic","aerobatic")



        client = Client("localhost:8080")
        client.port
        client.new_har('aerobatic')
        print(client.har)
        client.basic_authentication("aerobatic","aerobatic","aerobatic")

        time.sleep(3)
        #resp = requests.post('http://localhost:8080/proxy', {})
        #print(resp)
        #print(resp.content)
        #print(resp.json())

        #p = requests.put('http://localhost:8080/proxy/8086/har', {"initialPageRef": "aerobatic"})


        pass


if __name__ == "__main__":
    unittest.main()
