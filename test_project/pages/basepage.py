# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_page.py
# @Author   : Pluto.
# @Time     : 2020/10/18 14:34
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    _base_url = ""

    def __init__(self, driver_base=None):
        # 避免driver的重复实例化
        if driver_base is None:
            # 复用浏览器
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            # 1.添加remote复用类型注解 2.传参避免重新实例化
            self.driver: WebDriver = driver_base
        # 配置下放
        if self._base_url != "":
            self.driver.get(self._base_url)
        # 全局隐式等待
        self.driver.implicitly_wait(3)

    # 封装find_element
    def find(self, locator):
        # *解元组
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        return self.find(locator).click()

    def find_and_send_keys(self, locator, value):
        return self.find(locator).send_keys(value)

    # 封装find_elements
    def finds(self, locator):
        return self.driver.find_elements(*locator)

    # 自定义显示等待
    def wait_for_clickable(self,element):
        return WebDriverWait(self.driver,10).until(ec.element_to_be_clickable(element))
