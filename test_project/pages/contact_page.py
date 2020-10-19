# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2020/10/18 13:06
from time import sleep

from selenium.webdriver.common.by import By

from test_project.pages.basepage import BasePage


class ContactPage(BasePage):
    #添加成员按钮位置
    _add_member=(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    #获取成员列表
    _get_member_list=(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _cancel_member = (By.CSS_SELECTOR, ".js_btn_cancel")
    def go_to_add_member(self):
        # 解决循环导入问题
        from test_project.pages.add_member_page import AddMemberPage
        #循环查找元素
        while True:
            self.find_and_click(self._add_member)
            try:
                if self.find(self._cancel_member) is not None:
                    break
            except:
                pass
        return AddMemberPage(self.driver)

    def get_member_list(self):
        self.wait_for_clickable(self._get_member_list)
        ele = self.finds(self._get_member_list)
        return [name.text for name in ele]
