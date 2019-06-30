# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 界面方式选择.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/27 4:47 PM


from selenium import webdriver  # 导入浏览器驱动


# 有界面模式
driver = webdriver.Chrome()  # 初始化浏览器


# 无界面模式1，浏览器有一行会显示：chrome正受到自动测试软件的控制
chrome_options = webdriver.ChromeOptions()  # 浏览器初始化
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


# 无界面模式2，不会展示受控制
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=chrome_options)


# 退出模式选择
driver.quit()  # 整个浏览器退出
driver.close()  # 关闭界面，但不会退出浏览器