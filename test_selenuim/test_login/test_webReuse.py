# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_webReuse.py
# @Author   : Pluto.
# @Time     : 2020/10/16 18:42
# Generated by Selenium IDE
"""
Selenium IDE 录制脚本
修改为网页复用
chrome --remote-debugging-port=9222
127.0.0.1:9222
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWebReuse():
    def setup_method(self):
        # 网页复用
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        # 全局隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_webReuse(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("persion1")
        self.driver.find_element(By.ID, "memberAdd_acctid").click()
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("12345678")
        self.driver.find_element(By.ID, "memberAdd_phone").click()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13722222222")
        self.driver.find_element(By.LINK_TEXT, "保存").click()
        # assert
