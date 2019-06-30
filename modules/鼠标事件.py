# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 鼠标事件.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 3:07 PM


"""

鼠标事件的库在：selenium.webdriver.common.action_chains
    context_click()  # 右键单击
    double_click()  # 双击
    drag_and_drop()  # 鼠标按下的元素，鼠标释放的元素,拖动
    move_to_element()  # 鼠标悬停在一个元素上
    click_and_hold()  # 按下鼠标左键在一个元素上

"""

# 事例1：鼠标移动并显示二维码
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.jrj.com.cn/")
sleep(2)
source = driver.find_element_by_xpath(".//*[@id='appherw']")
ActionChains(driver).move_to_element(source).perform()
