# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: QQ邮箱登录.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 1:14 PM


from selenium import webdriver
import time

# 测试QQ邮箱登陆
def qqyouxiang():
    driver = webdriver.Chrome()
    driver.get('https://qzone.qq.com/')  # 获取网页

    user='qqzhanghao'
    password='qqmima'

    driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click() #选择账号密码登录

    driver.find_element_by_xpath('//*[@id="u"]').clear()

    driver.find_element_by_xpath('//*[@id="u"]').send_keys(user)

    driver.find_element_by_xpath('//*[@id="p"]').clear()

    driver.find_element_by_xpath('//*[@id="p"]').send_keys(password)

    driver.find_element_by_xpath('//*[@id="login_button"]').click()


qqyouxiang()
# 记录一下，测试失败，需要重新编写