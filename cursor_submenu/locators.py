# -*- coding: utf-8 -*-

# locators

MENU_WITH_SUB_MENU = "a[href='#example-1-tab-2']"

IFRAME_SUB_MENU = "div#example-1-tab-2 iframe"

SUB_MENU_ADAMSVILL =  "li#ui-id-2"



def get_menu_with_sub_menu():
    return MENU_WITH_SUB_MENU

def get_iframe_sub_menu():
    return IFRAME_SUB_MENU

def get_sub_menu(sub_menu_el):
    if sub_menu_el == "adamsvill":
        return SUB_MENU_ADAMSVILL
    return 0
