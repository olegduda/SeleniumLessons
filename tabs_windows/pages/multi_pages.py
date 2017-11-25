# -*- coding: utf-8 -*-

# multi pages way

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import MultipleWindows


class MultiPages(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver_wite = WebDriverWait(self.driver, 10)
        self.loc = MultipleWindows()


    def current_handle(self):
        return self.driver.current_window_handle


    def click_link(self):
        self.driver_wite.until(EC.element_to_be_clickable(self.loc.LINK_NEW_TAB)).click()

    def switch_to_frame(self):
        self.driver_wite.until(EC.frame_to_be_available_and_switch_to_it(self.loc.IFRAME_OMW_ONE))

    def clic_open_omp(self):
        self.driver_wite.until(EC.element_to_be_clickable(self.loc.OPEN_MULTIPLE_WINDOWS)).click()

    def get_link_text(self):
        return self.driver_wite.until(EC.element_to_be_clickable(self.loc.LINK_NEW_TAB)).text


    def goto_new_tab(self):
        current_handle = self.current_handle()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_handle :
                self.driver.switch_to.window(handle)
                break

    def goto_new_tab_text(self, link_name):
        current_handle = self.current_handle()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_handle :
                self.driver.switch_to.window(handle)
                if self.get_link_text() == link_name:
                    return True

