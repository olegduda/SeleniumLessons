# -*- coding: utf-8 -*-

# auth
from selenium.webdriver.support import expected_conditions as EC

from ..pages.locators import LoginPageLocators

class authSite():
    __login = "om8.info"
    __pass = "853m358o"

    def auth_login(self, driver, driver_wait):
        self.loc = LoginPageLocators()
        self.driver = driver
        self.driver_wait = driver_wait

        self.driver_wait.until(EC.element_to_be_clickable(self.loc.LOGIN_OPEN)).click()
        self.driver_wait.until(EC.element_to_be_clickable(self.loc.SET_LOGIN)).send_keys(self.__login)
        self.driver_wait.until(EC.element_to_be_clickable(self.loc.SET_PASS)).send_keys(self.__pass)
        self.driver_wait.until(EC.element_to_be_clickable(self.loc.SET_LOGIN)).click()
        self.driver_wait.until(EC.element_to_be_clickable(self.loc.SABMIT)).click()

