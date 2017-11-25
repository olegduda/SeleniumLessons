# -*- coding: utf-8 -*-

# locators

from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_OPEN = By.CSS_SELECTOR, 'a.fancybox[href="#login"]'
    SET_LOGIN = By.CSS_SELECTOR, "div[id='login'] input[name='username']"
    SET_PASS = By.CSS_SELECTOR, "div[id='login'] input[name='password']"
    SABMIT = By.CSS_SELECTOR, "div[id='login'] input[type='submit']"

class MultipleWindows():
    OPEN_MULTIPLE_WINDOWS = By.CSS_SELECTOR, "div.internal_navi a[href='#example-1-tab-4']"
    IFRAME_OMW_ONE = By.CSS_SELECTOR, "div#example-1-tab-4 iframe"
    LINK_NEW_TAB = By.CSS_SELECTOR, "div.farme_window a[href='#']"
