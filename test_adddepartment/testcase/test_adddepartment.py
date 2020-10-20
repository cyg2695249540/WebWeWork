# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_adddepartment.py
# @Author   : Pluto.
# @Time     : 2020/10/20 11:14
import allure
import pytest
import yaml

from test_adddepartment.page.main_page import MainPage


def get_datas():
    with open("../datas/addcontact.yml", encoding="utf-8") as f:
        department_datas = yaml.safe_load(f)
        adddepartment = department_datas["adddepartment"]
        case3 = department_datas["case3"]
        adddepartmentfail = department_datas["adddepartmentfail"]
        case4 = department_datas["case4"]
        return adddepartment, case3, adddepartmentfail, case4

@allure.feature("添加部门")
class TestAdddepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver.quit()
    @allure.feature("确认添加部门")
    @pytest.mark.parametrize("departmentname",get_datas()[0],ids=get_datas()[1])
    def test_add_department(self, departmentname):
        namelist = self.main.go_to_contact_page().go_to_adddepartment_page().adddepartment(
            departmentname).save_department().get_department_list()
        assert departmentname in namelist

    @allure.feature("取消添加部门")
    @pytest.mark.parametrize("departmentname", get_datas()[2], ids=get_datas()[3])
    def test_cancel_department(self, departmentname):
        namelist = self.main.go_to_contact_page().go_to_adddepartment_page().adddepartment(
            departmentname).cancel_department().get_department_list()
        assert departmentname not in namelist
