# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/19 13:15
from selenium.webdriver.common.by import By


from test_addmember.page.base_page import BasePage


class ContactPage(BasePage):
    _addmember_page = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    def go_to_addmember_page(self):
        from test_addmember.page.addmember_page import AddMemberPage
        while True:
            self.find_and_clike(self._addmember_page)
            try:
                if self.find(self._cancel) is not None:
                    break
            except:
                print("再次点击")

        return AddMemberPage(self.driver)

    def get_member_list(self):
        self.wait_for_clickable(self._member_list)
        ele = self.finds(self._member_list)
        return [name.text for name in ele]
