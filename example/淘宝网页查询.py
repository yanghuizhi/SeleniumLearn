# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 淘宝网页查询.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 1:06 PM

from selenium import webdriver
import time


# 测试淘宝网页输入字符并删除，再次输入并查询

def taobao():
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')  # 打开淘宝
    # print(driver.page_source)  # 输出网页代码
    input = driver.find_element_by_id('q')  # 获取输入框
    time.sleep(2)
    input.send_keys('我第一次输入字符')  # 输入字符
    time.sleep(1)
    input.clear()  # 清除输入字符
    input.send_keys('我第二次输入字符')  # 再次输入字符
    time.sleep(1)
    button = driver.find_element_by_class_name('btn-search')  # 获取搜索按钮
    button.click()  # 点击
    time.sleep(3)
    driver.close() # 关闭浏览器

taobao()