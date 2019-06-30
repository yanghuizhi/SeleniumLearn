# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 截取某个元素的图片.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 2:39 PM

# coding:utf-8
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

driver.save_screenshot('button.png')
element = driver.find_element_by_id("su")
print(element.location)                # 打印元素坐标
print(element.size)                    # 打印元素大小

left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']

im = Image.open('button.png')
im = im.crop((left, top, right, bottom))
im.save('button.png')