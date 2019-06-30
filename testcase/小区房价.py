# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 小区房价.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 1:24 PM

from selenium import webdriver

# 解析网页
html=brow.page_source
doc=pq(html)
house=doc('.resblock-list-wrapper li').items()

for i in house:
    house_Data={
        '小区':i.find('.name').text(),
        '房类':i.find('.resblock-type').text()

    }
