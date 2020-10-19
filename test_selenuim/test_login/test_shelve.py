# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_shelve.py
# @Author   : Pluto.
# @Time     : 2020/10/17 11:47
"""
使用shelve小型数据库实现cookie持久化存储
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestShelve():
    def setup_method(self):
        # #复用网页获取cookie
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver =webdriver.Chrome()
        # 全局隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_importContacts(self):
        # 点击导入通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 点击并添加上传文件
        self.driver.find_element(By.XPATH,
                                 "//input[@class='ww_fileImporter_fileContainer_uploadInputMask']").send_keys(
            "C:/Users/uiui/Desktop/txl.xlsx")
        # 验证上传文件是否正确
        assert "txl.xlsx" == self.driver.find_element(By.XPATH,
                                                      "//div[@class='ww_fileImporter_fileContainer_fileNames']").text
        sleep(3)

    def test_shelve(self):
        # # #获取cookies
        # cookies = self.driver.get_cookies()
        # db = shelve.open("./mydbs/cookies")
        # db["cookie"] = cookies
        # db.close()
        db = shelve.open("./mydbs/cookies")
        cookies=db["cookie"]
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 点击导入通讯录
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 点击并添加上传文件
        self.driver.find_element(By.XPATH, "//input[@class='ww_fileImporter_fileContainer_uploadInputMask']").send_keys(
            "C:/Users/uiui/Desktop/txl.xlsx")
        # 验证上传文件是否正确
        assert "txl.xlsx" == self.driver.find_element(By.XPATH,
                                                      "//div[@class='ww_fileImporter_fileContainer_fileNames']").text
        sleep(3)
