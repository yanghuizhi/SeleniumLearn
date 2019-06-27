# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: __init__.py.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/27 4:47 PM


from selenium import webdriver  # 导入浏览器驱动

""" 无界面模式 """

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.close()

""" 有界面模式 """

browser = webdriver.Chrome()
browser.close()
