#coding=utf-8


from bs4 import BeautifulSoup
from scrapy_new.items import ScrapyNewItem
import requests


#公共方法，用于获取某些数据
def publicone(self,title,title_url,clwsurl):
    item = ScrapyNewItem()
    news = requests.get(url=clwsurl)
    Soup_guoji = BeautifulSoup(news.text, 'lxml')  # 使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
    newstitleinfo = Soup_guoji.find('div', class_='column-title-border').find('a')
    headlineinfo = newstitleinfo.get_text() + "新闻"
    messageinfo = Soup_guoji.find('div', class_="l-left-col col-mod").find_all('a')
    message_urllist = []
    message_titlelist = []
    for guojimessage in messageinfo:
        message_title = guojimessage.get_text()
        message_url = guojimessage['href']
        message_titlelist.append(message_title)
        message_urllist.append(message_url)
    return headlineinfo,message_titlelist,message_urllist


def publictwo(self,title,title_url,clwsurl):
    item = ScrapyNewItem()
    news = requests.get(url=clwsurl)
    Soup = BeautifulSoup(news.text, 'lxml')
    headlineinfo = Soup.find('div', class_='column-title-border').get_text()
    body = Soup.find('div', class_='b-left').find_all('a')
    message_urllist = []
    message_titlelist = []
    for messageinfo in body:
        message_title = messageinfo.get_text()
        message_url = messageinfo['href']
        message_titlelist.append(message_title)
        message_urllist.append(message_url)
    return headlineinfo, message_titlelist, message_urllist