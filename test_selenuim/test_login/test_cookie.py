# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_cookie.py
# @Author   : Pluto.
# @Time     : 2020/10/16 19:13
"""
使用cookie登录
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testcookie():
    def setup_method(self):
        # # 网页复用获取当前带有登录信息的cookie
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 全局隐式等待
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        # #获取带有登录信息的cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'yCxQf6A8c_nR0XkrBWU7OQeTFx2JTjs6joSqZSDiYkYTXedBbQI4__Bi1pqj4rjfaEnytKn1puAQjfg5atuFZDN3nxo4cC-fRXPpgY60sSyOqaui-E4yFvCvh1_hPcp2CZDqpjIQzrHy9MVU50J3xwjB1vg75rOaeg4yH3SceuN0XGArSX05FJqrM90l58YKfQYhvf_hCnNED_CKRzKmjaJminQSXiVLwHvBdmd5nlaqoeY1CDouwmIGTJUAahSGv282EBFWlh2QSK6DUqJ1Fw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1602986103, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2105122832.1602829200'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634365197, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
             'value': '1601292835,1601353994,1602829198'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605491717, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1665971703, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1695920304.1600253078'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
             'value': '95ef3e2304d9bb394d1041b90975880d0f73d7c601ce3d060b4320df93f65339'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a2828257'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
             'value': 'GELU7mmCmN'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324964157309'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': True, 'value': '1994772480'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974602, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
             'secure': True, 'value': 'sites'},
            {'domain': '.qq.com', 'expiry': 1917515580, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': True, 'value': '28820859b5600ad2'},
            {'domain': '.qq.com', 'expiry': 2230974602, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': True,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974602, 'httpOnly': True, 'name': 'wwrtx.refid',
             'path': '/', 'secure': True, 'value': '29352789632675821'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': True, 'value': '3737722324'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974602, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '43b3gcp'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851206530025'},
            {'domain': 'work.weixin.qq.com', 'expiry': 2230974602, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '43b3gcp'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'eDFCKFCe06cak8OFW0Dwq_X5WdSKsHUh4LmMFgYiuOyBrMiaHb5iNHVK58ajd3SY'},
            {'domain': '.work.weixin.qq.com', 'expiry': 2230974602, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'}]
        # 打开页面，提示需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 传入cookie,addcookie方法只支持dict格式,将列表转化为多行字典
        for cookie in cookies:
            # add_cookie不支持浮点数，可以把无关参数expiry删除
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开，已带有cookie信息的页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
