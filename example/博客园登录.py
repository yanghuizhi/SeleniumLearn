# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 博客园登录.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/30 9:53 AM


from selenium import webdriver
from time import sleep

# 博客园登录实战
def bokeyuan():
    driver = webdriver.Chrome()
    driver.get("https://www.cnblogs.com/")
    driver.find_element_by_xpath('//*[@id="span_userinfo"]/a[1]').click()
    driver.find_element_by_xpath('//*[@id="LoginName"]').send_keys("账号")
    driver.find_element_by_xpath('//*[@id="Password"]').send_keys('密码')
    driver.find_element_by_xpath('//*[@id="submitBtn"]/span[1]').click()
    sleep(2)
    driver.refresh()

bokeyuan()