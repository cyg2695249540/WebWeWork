# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : adddepartment_page.py
# @Author   : Pluto.
# @Time     : 2020/10/20 11:15
from selenium.webdriver.common.by import By

from test_adddepartment.page.base_page import BasePage
from test_adddepartment.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    _department_name = (By.CSS_SELECTOR, "[name='name']")
    _click_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _jstree_anchor = (By.CSS_SELECTOR, '.qui_dropdownMenu.ww_dropdownMenu.member_colLeft.js_party_list_container')
    _save_button = (By.CSS_SELECTOR, "[d_ck='submit']")
    _cancel_button = (By.CSS_SELECTOR, "[d_ck='cancel']")

    def adddepartment(self, department):
        self.find_and_send_keys(self._department_name, department)
        self.find_and_clike(self._click_department)
        departmentlist = self.finds(self._jstree_anchor)
        if departmentlist is not None:
            departmentlist[0].click()
        return self

    def save_department(self):
        self.find_and_clike(self._save_button)
        return ContactPage(self.driver)

    def cancel_department(self):
        self.find_and_clike(self._cancel_button)
        return ContactPage(self.driver)
