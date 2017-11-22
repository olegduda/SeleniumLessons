# -*- coding: utf-8 -*-

# Cursor submenu working

import unittest
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .auth_login import *
from .locators import *

import time


class testSubmenuOpen(unittest.TestCase):

    __page_load = "http://way2automation.com/way2auto_jquery/menu.php"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.driver.get(self.__page_load)
        authSite().auth_login(self.driver)
        self.driver.get(self.__page_load)

    def tearDown(self):
        self.driver.quit()


    def testSubmenuVisible(self):

        driver_wait = WebDriverWait(self.driver, 10)

        driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_menu_with_sub_menu()))).click()

        driver_wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, get_iframe_sub_menu())))

        sum_menu_el = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,get_sub_menu("adamsvill"))))
        ActionChains(self.driver).move_to_element(sum_menu_el).perform()

        self.assertTrue(self.driver.find_element_by_css_selector(get_sub_menu("adamsvill")).is_displayed(),"not visible")


if __name__ == "__main__":
    unittest.main()
