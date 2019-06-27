# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 20190627-基本使用.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/27 4:53 PM

from selenium import webdriver  # 导入浏览器驱动
import time

browser  = webdriver.Chrome() # 初始化

browser.get('https://www.taobao.com')

input = browser.find_element_by_id('q')  # 获取输入框

input.send_keys('iPhone')  # 输入

time.sleep(3)

browser.close()