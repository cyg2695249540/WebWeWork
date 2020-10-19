# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/19 13:14
from selenium.webdriver.common.by import By

from test_addmember.page.addmember_page import AddMemberPage
from test_addmember.page.base_page import BasePage
from test_addmember.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    _addmember_page=(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)")
    _contact_page=(By.ID,"menu_contacts")

    def go_to_addmember_page(self):
        self.find_and_clike(self._addmember_page)
        return AddMemberPage(self.driver)

    def go_to_contact_page(self):
        self.find_and_clike(self._contact_page)
        return ContactPage(self.driver)
