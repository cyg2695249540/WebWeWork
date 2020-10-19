# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2020/10/18 13:06

from selenium.webdriver.common.by import By
from test_project.pages.add_member_page import AddMemberPage
from test_project.pages.basepage import BasePage
from test_project.pages.contact_page import ContactPage


class MainPage(BasePage):
    # 主页
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 点击添加成员位置
    _go_to_add_member = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    # 点击通讯录位置
    _go_to_contact = (By.ID, "menu_contacts")

    def go_to_add_member(self):
        self.find_and_click(self._go_to_add_member)
        return AddMemberPage(self.driver)

    def go_to_contact(self):
        self.find_and_click(self._go_to_contact)
        return ContactPage(self.driver)
