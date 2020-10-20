# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : addmember_page.py
# @Author   : Pluto.
# @Time     : 2020/10/18 13:07

from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    #添加姓名位置
    _username=(By.ID, "username")
    #添加账号位置
    _memberAdd_acctid=(By.ID, "memberAdd_acctid")
    #添加联系电话位置
    _memberAdd_phone=(By.ID, "memberAdd_phone")
    #保存按钮位置
    _save_member=(By.CSS_SELECTOR, ".js_btn_save")
    #取消按钮位置
    _cancel_member=(By.CSS_SELECTOR, ".js_btn_cancel")
    #提示框-离开此页位置
    _leave=(By.CSS_SELECTOR, "[node-type='cancel']")
    def add_member(self, username, acctid, phone):
        self.find_and_send_keys(self._username,username)
        self.find_and_send_keys(self._memberAdd_acctid,acctid)
        self.find_and_send_keys(self._memberAdd_phone,phone)
        # 返回当前页面时依然实现链式调用
        return self

    def save_member(self):
        self.find_and_click(self._save_member)
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find_and_click(self._cancel_member)
        self.find_and_click(self._leave)
        return ContactPage(self.driver)
