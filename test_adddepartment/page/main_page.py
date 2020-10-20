# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/20 11:14
from time import sleep

from selenium.webdriver.common.by import By

from test_adddepartment.page.addmember_page import AddmemberPage
from test_adddepartment.page.base_page import BasePage
from test_adddepartment.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _addmember_button = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    _contact_butto = (By.CSS_SELECTOR, "[id='menu_contacts']")

    def go_to_addmember_page(self):
        self.find_and_clike(self._addmember_button)
        return AddmemberPage(self.driver)

    def go_to_contact_page(self):
        self.find_and_clike(self._contact_butto)
        return ContactPage(self.driver)
