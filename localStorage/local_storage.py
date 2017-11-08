# -*- coding: utf-8 -*-

# localStorage work
# enter data in LOGIN and PASS


import unittest
from selenium import webdriver
import json

import time

class testLocalStore(unittest.TestCase):

    PAGE_LOAD = "https://maketalents.simbirsoft1.com/auth/login/"
    LOGIN = ""
    PASS = ""


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.driver.get(self.PAGE_LOAD)

    def tearDown(self):
        self.driver.quit()

    def testSearch(self):

        login = self.driver.find_element_by_css_selector("input.md-input[ng-model='vm.auth.username']")
        login.send_keys(self.LOGIN)
        password = self.driver.find_element_by_css_selector("input.md-input[ng-model='vm.auth.pass']")
        password.send_keys(self.PASS)
        self.driver.find_element_by_css_selector("button.md-button[type='submit']").click()

        self.driver.find_element_by_css_selector("div[adf-id='6']")

        local_store = self.driver.execute_script("return localStorage.getItem('ngStorage-user')")
        ss_local_store = json.loads(local_store)

        print("firstName: " + ss_local_store['firstName'])
        print("lastName: " + ss_local_store['employee']['lastName'])
        print("phone: " + ss_local_store['employee']['phone'])
        print("email: " + ss_local_store['employee']['email'])
        print("skype: " + ss_local_store['employee']['skype'])
        print("englishLevel: " + str(ss_local_store['employee']['englishLevel']))
        print("roles: " + str(ss_local_store['roles']))


if __name__ == "__main__":
    unittest.main()
