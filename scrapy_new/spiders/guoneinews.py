#coding=utf-8

from bs4 import BeautifulSoup
from scrapy_new.items import ScrapyNewItem
import scrapy
from scrapy.selector import Selector
import requests,random
from scrapy_new.spiders.pubulic import publictwo
from scrapy_new.spiders.title import titlemessage



class guoneinews(scrapy.Spider):
    global title,title_url
    title = titlemessage()[0][1]
    title_url = titlemessage()[1][1]
    name = "guonei"   #唯一标识
    allowed_domains = ["news.baidu.com"]     #允许的域名
    start_urls = [title_url]    #首次进入的链接


    def parse(self,response):
        selector = Selector(response=response)
        item = ScrapyNewItem()
        gangaotai_url = "https://news.baidu.com/widget?id=GangAoTai&channel=guonei&t=1559635605942"   #港澳台地址
        shizheng_url = "https://news.baidu.com/widget?id=ShiZheng&channel=guonei&t=1559642375649"  #时政要闻
        zuixin_url = "https://news.baidu.com/widget?id=LatestNews&channel=guonei&t=1559643233939"   #最新新闻

        # 得到焦点新闻里的所有新闻信息
        headlineinfo_jiaodian = selector.xpath('//*[@id="col_focus"]/div[1]/div[1]/div/h2/span[1]/text()').extract()
        body = selector.xpath('//*[@id="col_focus"]/div[1]/div[2]')
        for messageinfo in body:
            message_titlelist = messageinfo.css('ul a::text').extract()
            message_urllist = messageinfo.css('ul a::attr(href)').extract()
            for info1,info2 in zip(message_titlelist,message_urllist):
                message_title = info1
                message_url = info2
                item['message_title'] = message_title
                item['message_url'] = message_url
                item['headlineinfo'] = headlineinfo_jiaodian
                item['title'] = title
                item['title_url'] = title_url
                yield item

        # 得到即时新闻的所有新闻信息
        headlineinfo_jishi = selector.xpath('//*[@id="internal-aside-video"]/div[1]/h3/text()').extract()
        body = selector.xpath('//*[@id="instant-news"]')
        for messageinfo in body:
            message_titlelist = messageinfo.css('ul a::text').extract()
            message_urllist = messageinfo.css('ul a::attr(href)').extract()
            for info1,info2 in zip(message_titlelist,message_urllist):
                message_title = info1
                message_url = info2
                item['message_title'] = message_title
                item['message_url'] = message_url
                item['headlineinfo'] = headlineinfo_jishi
                item['title'] = title
                item['title_url'] = title_url
                yield item

        # 港澳台新聞（直接调用写的方法进行存储）
        gangaotainews = publictwo(self,title,title_url,gangaotai_url)
        for message_title,message_url in zip(gangaotainews[1],gangaotainews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = gangaotainews[0][1:4]+"新闻"
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 最新新聞
        news = requests.get(url=zuixin_url)
        Soup = BeautifulSoup(news.text, 'lxml')
        headlineinfo = Soup.find('div', class_='column-title-border').get_text()
        body = Soup.find('div', id='latest-news').find_all('a')
        print(body)
        for messageinfo in body:
            item['message_title'] = messageinfo.get_text()
            item['message_url'] = messageinfo['href']
            item['headlineinfo'] = headlineinfo[:5]
            item['title'] = title
            item['title_url'] = title_url
            yield item