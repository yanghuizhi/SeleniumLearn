# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 文件下载弹框处理.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 2:47 PM


from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time

driver = webdriver.Firefox()
driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")

time.sleep(3)
# 默认在取消按钮上，先切换到保存文件上
k = PyKeyboard()

# 发送tab
k.press_key(k.tab_key)
k.release_key(k.tab_key)

time.sleep(3)
# 发送回车