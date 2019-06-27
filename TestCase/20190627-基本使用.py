# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 20190627-基本使用.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/27 4:53 PM


from selenium import webdriver  # 导入浏览器驱动
import time

browser  = webdriver.Chrome() # 初始化

browser.get('https://www.taobao.com')  # 用get方法请求网页

print(browser.page_source)  # 输出网页代码

time.sleep(3)

browser.close()  # 关闭浏览器