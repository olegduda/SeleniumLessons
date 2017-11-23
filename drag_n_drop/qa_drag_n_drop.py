# -*- coding: utf-8 -*-

# Drag and Drop working

import unittest
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .auth_login import *
from .locators import *


class testSubmenuOpen(unittest.TestCase):

    __page_load_start = "http://way2automation.com/way2auto_jquery/index.php"
    __page_load = "http://way2automation.com/way2auto_jquery/droppable.php"


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(12)
        self.driver.get(self.__page_load_start)
        authSite().auth_login(self.driver)
        self.driver.get(self.__page_load)

    def tearDown(self):
        self.driver.quit()


    def testDragAndDrop(self):

        driver_wait = WebDriverWait(self.driver, 10)

        driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_menu_def_fun()))).click()

        driver_wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, get_iframe_dropp())))

        el_dropp = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, get_dropp())))
        text_before_dropp = el_dropp.text

        el_dragg = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, get_dragg())))

        ActionChains(self.driver).drag_and_drop(el_dragg, el_dropp).perform()
        el_dropp = driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, get_dropp())))
        text_after_dropp = el_dropp.text

        self.assertTrue(text_before_dropp != text_after_dropp ,"Not Drag_and_Drop")


if __name__ == "__main__":
    unittest.main()
