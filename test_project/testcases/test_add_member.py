# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_add_member.py
# @Author   : Pluto.
# @Time     : 2020/10/18 13:15
import time

import allure
import pytest
import yaml

from test_project.pages.main_page import MainPage


def get_datas():
    with open("../datas/addcontact.yml", encoding="utf-8") as f:
        contact_datas = yaml.safe_load(f)
        addcontact = contact_datas["add"]
        case1 = contact_datas["case1"]
        addcontactfail = contact_datas["addfail"]
        case2 = contact_datas["case2"]

    return addcontact, case1, addcontactfail,case2

@allure.feature("添加成员模块")
class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()

    # 添加成员成功
    @allure.feature("添加成员成功")
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[0], ids=get_datas()[1])
    def test_add_member(self, username, acctid, phone):
        # 1.首页跳转添加成员页面 2.添加成员
        namelist = self.main.go_to_add_member().add_member(username, acctid, phone).save_member().get_member_list()
        assert username in namelist

    # 添加成员失败
    @allure.feature("添加成员失败")
    @pytest.mark.parametrize("username,acctid,phone", get_datas()[2],ids=get_datas()[3])
    def test_add_member_fail(self, username, acctid, phone):
        # 1.首页跳转添加成员页面 2.添加成员
        namelist = self.main.go_to_add_member().add_member(username, acctid, phone).cancel_member().get_member_list()
        assert username not in namelist

    #通讯录添加成员成功
    @allure.feature("通讯录添加成员成功")
    @pytest.mark.parametrize("username,acctid,phone",  get_datas()[0], ids=get_datas()[1])
    def test_contact_add_member(self, username, acctid, phone):
        # 1.首页跳转通讯录页面 2.跳转添加成员页面 3.添加成员
        namelist = self.main.go_to_contact().go_to_add_member().add_member(username, acctid,
                                                                           phone).save_member().get_member_list()
        assert username in namelist
