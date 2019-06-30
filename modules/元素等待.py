# !/usr/bin/env python
# -*- coding: utf-8 -*-
# File: 元素等待.py
# Author: Leo_yanghuizhi
# Email: 347818169@qq.com.com
# Time: 2019/6/29 2:51 PM


"""
    我们在做web网站自动化测试的过程中，会经常遇到web应用程序使用了AJAX技术。
    当浏览器加载页面的时候，而页面上的元素还未同时被加载完成，那么我们此时进行
元素的定位往往会出现错误，影响我们在自动化测试工作进程。这样在加载某个元素延迟而
造成了ElementNotVisibleException的报错，就会降低自动化脚本的稳定性。
    如何解决这个问题呢？我们可以通过设置元素等待改善这种问题造成的负面影响。
    webdriver为我们提供了三种等待方法
"""

# 1、强制等待

from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
sleep(3) # 强制等待
print(driver.current_url)
driver.quit()

# 这种叫强制等待，不管你浏览器是否加载完了，程序都得等待3秒，3秒一到，继续执行下面的代码，
# 作为调试很有用，有时候也可以在代码里这样等待，不过不建议总用这种等待方式，太死板，严重影响程序执行速度。

# 2、隐性等待

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(20) # 隐性等待，最长等待20s
driver.get('https://www.baidu.com/')
print(driver.current_url)
driver.quit()

# 隐形等待是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，
# 然后执行下一步。但是这里有一个弊端，那就是程序会一直等待整个页面加载完成，也就是我们可以看到浏览器
# 标签栏那个小圈不再转，才会执行下一步，通常页面想要的元素早就在加载完成了，但是因为个别js之类的东西
# 特别慢，得等到页面全部完成才能执行下一步，那我们需要主题元素出现就可以下一步该如何去做呢，那就要看
# selenium提供的另一种等待方式——显性等待wait了。
# 这里需要强调的是：隐性等待对整个driver的周期都起作用，所以只要设置一次即可。


# 3、显性等待

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20) # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
driver.get('https://www.baidu.com/')
locator = (By.ID, 'su')
try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
finally:
    driver.close()

# 第三种方法就是显性等待，WebDriverWait,配合该类的until()和until_not()方法，就能够根据判断
# 条件来进行灵活地等待了。它主要的意思是：程序每隔xx秒看以下条件是否满足，如果条件成立了，则执行
# 下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
# 上例中，我们设置了隐性等待和显性等待，在其他操作中，隐性等待起决定性作用，
# 在WebDriverWait..中显性等待起主要作用，
# 但要注意的是：最长的等待时间取决于两者之间的大者，如果隐性等待时间 > 显性等待时间，
# 则该句代码的最长等待时间等于隐性等待时间。
