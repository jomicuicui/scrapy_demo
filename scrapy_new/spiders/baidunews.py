#coding=utf-8
from bs4 import BeautifulSoup
from scrapy_new.items import ScrapyNewItem
import scrapy
from scrapy.selector import Selector
from scrapy_new.spiders.pubulic import publicone
from scrapy_new.spiders.title import titlemessage


class baidunews(scrapy.Spider):
    global title,title_url
    title = titlemessage()[0][0]
    title_url = titlemessage()[1][0]
    name = "baidunews"   #唯一标识
    allowed_domains = ["news.baidu.com"]     #允许的域名
    start_urls = [title_url]     #首次进入的链接

    #获取首页的新闻信息
    def parse(self,response):
        selector = Selector(response=response)
        item = ScrapyNewItem()
        guonei_url = "https://news.baidu.com/widget?id=civilnews&t=1558504498350"    #國内新聞
        guoji_url = "https://news.baidu.com/widget?id=InternationalNews&t=1558510214746"  # 国际新闻
        yulei_url = "https://news.baidu.com/widget?id=EnterNews&t=1559615373212"    #娱乐新闻
        tiyu_url = "https://news.baidu.com/widget?id=SportNews&t=1559626085872"   #体育新闻
        caijing_url = "https://news.baidu.com/widget?id=FinanceNews&t=1559626085888"    #财经新闻
        keji_url = "https://news.baidu.com/widget?id=TechNews&t=1559626085916"    #科技新闻
        junshi_url = "https://news.baidu.com/widget?id=MilitaryNews&t=1559626085956"  #军事新闻
        hulianwang_url = "https://news.baidu.com/widget?id=InternetNews&t=1559626085973"  #互联网新闻
        tansuo_url = "https://news.baidu.com/widget?id=DiscoveryNews&t=1559626086127"    #探索新闻
        nvren_url = "https://news.baidu.com/widget?id=LadyNews&t=1559626086243"   #女人新闻
        jiankang_url = "https://news.baidu.com/widget?id=HealthNews&t=1559626086283"   #健康新闻

        # 得到热点新闻里的所有新闻信息
        headlineinfo_redian = selector.xpath('//*[@id="headline-tabs"]/ul/li/a/text()').extract()
        body = selector.xpath('//*[@id="pane-news"]')
        for messageinfo in body:
            message_titlelist = messageinfo.css('ul a::text').extract()
            message_urllist = messageinfo.css('ul a::attr(href)').extract()
            for info1,info2 in zip(message_titlelist,message_urllist):
                message_title = info1
                message_url = info2
                item['message_title'] = message_title
                item['message_url'] = message_url
                item['headlineinfo'] = headlineinfo_redian
                item['title'] = title
                item['title_url'] = title_url
                yield item

        # 得到百家号的所有新闻信息
        headlineinfo_baijiahao = selector.xpath('//*[@id="baijia"]/div[1]/div/h2/span[1]/text()').extract()
        body_baijiahao = selector.xpath('//*[@id="baijia"]')
        for messageinfo_baijiahao in body_baijiahao:
            message_titlelist = messageinfo_baijiahao.css('div a::text').extract()
            message_urllist = messageinfo_baijiahao.css('div a::attr(href)').extract()
            for info1, info2 in zip(message_titlelist, message_urllist):
                message_title = info1
                message_url = info2
                item['message_title'] = message_title
                item['message_url'] = message_url
                item['headlineinfo'] = headlineinfo_baijiahao
                item['title'] = title
                item['title_url'] = title_url
                yield item

        #国内新聞（直接调用写的方法进行存储）
        guoneinews = publicone(self,title,title_url,guonei_url)
        for message_title,message_url in zip(guoneinews[1],guoneinews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = guoneinews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        #国际新聞（直接调用写的方法进行存储）
        guojinews = publicone(self,title,title_url,guoji_url)
        for message_title,message_url in zip(guojinews[1],guojinews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = guojinews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        #娱乐新闻（直接调用写的方法进行存储）
        yulenews = publicone(self,title,title_url,yulei_url)
        for message_title,message_url in zip(yulenews[1],yulenews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = yulenews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        #体育新闻（直接调用写的方法进行存储）
        tiyunews = publicone(self,title,title_url,tiyu_url)
        for message_title,message_url in zip(tiyunews[1],tiyunews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = tiyunews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        #财经新闻（直接调用写的方法进行存储）
        caijingnews = publicone(self,title,title_url,caijing_url)
        for message_title,message_url in zip(caijingnews[1],caijingnews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = caijingnews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        #科技新闻（直接调用写的方法进行存储）
        kejinews = publicone(self,title,title_url,keji_url)
        for message_title,message_url in zip(kejinews[1],kejinews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = kejinews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 军事新闻（直接调用写的方法进行存储）
        junshinews = publicone(self, title, title_url, junshi_url)
        for message_title, message_url in zip(junshinews[1], junshinews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = junshinews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 互联网新闻（直接调用写的方法进行存储）
        hulianwangnews = publicone(self, title, title_url, hulianwang_url)
        for message_title, message_url in zip(hulianwangnews[1], hulianwangnews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = hulianwangnews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 探索新闻（直接调用写的方法进行存储）
        tansuonews = publicone(self, title, title_url, tansuo_url)
        for message_title, message_url in zip(tansuonews[1], tansuonews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = tansuonews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 女人新闻（直接调用写的方法进行存储）
        nvrennews = publicone(self, title, title_url, nvren_url)
        for message_title, message_url in zip(nvrennews[1], nvrennews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = nvrennews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

        # 健康新闻（直接调用写的方法进行存储）
        jiankangnews = publicone(self, title, title_url, jiankang_url)
        for message_title, message_url in zip(jiankangnews[1], jiankangnews[2]):
            item['message_title'] = message_title
            item['message_url'] = message_url
            item['headlineinfo'] = jiankangnews[0]
            item['title'] = title
            item['title_url'] = title_url
            yield item

