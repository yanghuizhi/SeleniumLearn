# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 百度表情包下载.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 1:40 PM

import urllib
# path为要保存图片的文件夹
def downloadByHttp(url,path="/Users/mac/Pictures/spiderImg/"):
    # 截取文件名，避免文件名过长只截取最后20位
    fileName = url.split("/")[-1:][0][-20:]
    # 获取文件参数
    conn = urllib.urlopen(url)
    # 获取文件后缀名
    sub = conn.headers['Content-Type'].split("/")[-1:][0]
    print('sss:',sub)
    conn.close()
    # 如果这个超链接不包含后缀名，则加上一个后缀名
    if fileName.find(".") == -1:
        fileName = fileName+sub
    print(fileName)
    print("downloading with urllib")
    urllib.urlretrieve(url, path+fileName)

from selenium import webdriver
from NetUtil import download
class ImgSpider(object):
    # wd 搜索的关键字，maxPage最大下载的页数
    def __init__(self, wd="", maxPage = 5):
        # 百度图片搜索的http请求
        self.url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+wd
        # 打开火狐浏览器
        self.wb = webdriver.Firefox()
        # 设置最大下载你页数
        self.deep = maxPage
        self.start = 1
    #     打开第一页
    def first(self):
        # 打开url获取第一页结果
        self.wb.get(self.url)
        # 解析网页
        self.parse()
        # 读取下一页
        self.onNext()

    #     递归读取下一页，直到条件不满足
    def onNext(self):
        # 当前页码加1
        self.start += 1
        # 解析网页
        self.parse()
        # 通过xpath方法匹配页码指示器
        element = self.wb.find_element_by_xpath("//div[@id='page']")
        for el in element.find_elements_by_xpath(".//span[@class='pc']"):
            # 获取页码
            str = el.text
            num = int(str)
            # 比较页码，不满足条件则关闭程序
            if num > self.deep:
                self.close()
            #     继续执行下一页操作
            if num == self.start:
                el.click()
                self.onNext()
    #      解析下载图片
    def parse(self):
        # 通过xpath匹配当前网页的所有图片的最上层节点
        imgs = self.wb.find_element_by_xpath('''//div[@id="wrapper"]''')
        i = 0
        # 匹配所有的图片节点，遍历下载
        for img in imgs.find_elements_by_xpath(".//img"):
            i = i + 1
            # 获取img标签的连接
            url = img.get_attribute("src")
            print(url)
            # 给下载模块下载图片
            download.downloadByHttp(url)
    #关闭爬虫
    def close(self):
        self.wb.quit()
        exit()
#开始抓取数据 关键字 和 最大页数
spider = ImgSpider("表情包", 5)
spider.first()