# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_page.py
# @Author   : Pluto.
# @Time     : 2020/10/19 13:15
from selenium.webdriver.common.by import By

from test_addmember.page.base_page import BasePage
from test_addmember.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")
    _acctid = (By.ID, "memberAdd_acctid")
    _phone = (By.ID, "memberAdd_phone")
    _save_member = (By.CSS_SELECTOR, ".js_btn_save")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave=(By.CSS_SELECTOR,"[node-type='cancel']")

    def addmember(self, username, acctid, phone):
        self.find_and_send_keys(self._username, username)
        self.find_and_send_keys(self._acctid, acctid)
        self.find_and_send_keys(self._phone, phone)
        return self

    def save_member(self):
        self.find_and_clike(self._save_member)
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find_and_clike(self._cancel_member)
        self.find_and_clike(self._leave)
        return ContactPage(self.driver)
