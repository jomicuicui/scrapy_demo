# -*- coding: utf-8 -*-
# @Time : 2017/1/1 17:51
# @Author : woodenrobot
from scrapy import cmdline
import os,time

#如果是执行单个文件的话，可以使用以下方法
# # name = 'baidunews'
# # cmd = 'scrapy crawl {0}'.format(name)
# # cmdline.execute(cmd.split())

#如果是同时爬取多个文件的话，使用以下方法
os.system("scrapy crawl baidunews")
time.sleep(2)
os.system("scrapy crawl guonei")

