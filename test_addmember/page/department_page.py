# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department_page.py
# @Author   : Pluto.
# @Time     : 2020/10/19 15:21
from selenium.webdriver.common.by import By

from test_addmember.page.base_page import BasePage
from test_addmember.page.contact_page import ContactPage


class DepartmentPage(BasePage):
    _department_name = (By.CSS_SELECTOR, ".ww_inputText:nth-child(2)")
    _click_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _jstree_anchor = (By.CSS_SELECTOR, '.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container')
    _save_button = (By.CSS_SELECTOR, "[d_ck='submit']")
    _cancel_button = (By.CSS_SELECTOR, "[d_ck='cancel']")

    def add_new_department(self, departmentname):
        self.find_and_send_keys(self._department_name, departmentname)
        self.find_and_clike(self._click_department)
        department_list=self.finds(self._jstree_anchor)
        if department_list is not None:
            department_list[0].click()
        return self

    def save_department(self):
        self.find_and_clike(self._save_button)
        return ContactPage(self.driver)

    def cancel_department(self):
        self.find_and_clike(self._cancel_button)
        return ContactPage(self.driver)

