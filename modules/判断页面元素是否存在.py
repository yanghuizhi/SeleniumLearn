# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 判断页面元素是否存在.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 2:36 PM

# 这个可以说是被问烂的题了，判断元素存在方法有三种：

# 方法一，用try…except…

def is_element_exsist(driver, locator):
    '''
    判断元素是否存在,存在返回True,不存返回False
    :param locator: locator为元组类型，如("id", "yoyo")
    :return: bool值，True or False
    '''
    try:
        driver.find_element(*locator)
        return True
    except Exception as msg:
        print("元素%s找不到：%s" % (locator, msg))
        return False

if __name__ == '__main__':
    loc1 = ("id", "yoyo")  # 元素1
    print(is_element_exsist(driver, loc1))


# 方法二：用elements定义一组元素方法

def is_element_exsist1(driver, locator):
    '''
    判断元素是否存在,存在返回True,不存返回False
    :param locator: locator为元组类型，如("id", "yoyo")
    :return: bool值，True or False
    '''
    eles = driver.find_elements(*locator)
    if len(eles) < 1:
        return False
    else:
        return True

if __name__ == '__main__':
    loc1 = ("id", "yoyo")  # 元素1
    print(is_element_exsist1(driver, loc1))

# (强烈推荐！)方法三：结合WebDriverWait和expected_conditions判断

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
def is_element_exsist2(driver, locator):
    '''
    结合WebDriverWait和expected_conditions判断元素是否存在,
    每间隔1秒判断一次，30s超时，存在返回True,不存返回False
    :param locator: locator为元组类型，如("id", "yoyo")
    :return: bool值，True or False
    '''
    try:
        WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located(locator))
        return True
    except:
        return False
if __name__ == '__main__':
    loc1 = ("id", "yoyo")  # 元素1
    print(is_element_exsist2(driver, loc1))