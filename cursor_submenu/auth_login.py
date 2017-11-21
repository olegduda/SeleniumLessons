# -*- coding: utf-8 -*-

# auth

class authSite():
    __login = "om8.info"
    __pass = "853m358o"

    def auth_login(self, driver):
        self.driver = driver
        self.driver.find_element_by_css_selector("a.fancybox[href='#login']").click()
        self.driver.find_element_by_css_selector("div[id='login'] input[name='username']").send_keys(self.__login)
        self.driver.find_element_by_css_selector("div[id='login'] input[name='password']").send_keys(self.__pass)
        self.driver.find_element_by_css_selector("div[id='login'] input[name='username']").click()
        self.driver.find_element_by_css_selector("div[id='login'] input[type='submit']").click()

