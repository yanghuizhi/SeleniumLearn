# !/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver

driver = webdriver.Chrome()  # 初始化浏览器


# —— —— —— —— 单个元素定位 —— —— —— ——

driver.find_element_by_id()  # 通过 id 定位
driver.find_element_by_name()  # 通过name定位
driver.find_element_by_xpath()	# 通过绝对路径定位
driver.find_element_by_tag_name()  # 通过标签名定位
driver.find_element_by_link_text()  # 通过文本链接定位
driver.find_element_by_class_name()  # 通过class name定位
driver.find_element_by_css_selector()  # 通过css选择器定位
driver.find_element_by_partial_link_text()  # 通过文本链接的一部分定位


# —— —— —— —— 多个元素定位 —— —— —— ——

driver.find_elements_by_id()  # 通过 id 定位
driver.find_elements_by_name()  # 通过name定位
driver.find_elements_by_xpath()	# 通过绝对路径定位
driver.find_elements_by_tag_name()  # 通过标签名定位
driver.find_elements_by_link_text()  # 通过文本链接定位
driver.find_elements_by_class_name()  # 通过class name定位
driver.find_elements_by_css_selector()  # 通过css选择器定位
driver.find_elements_by_partial_link_text()  # 通过文本链接的一部分定位


