#coding=utf-8

from bs4 import BeautifulSoup
import requests

#获取分类的title名称和地址供后面使用
def titlemessage():
    url = "https://news.baidu.com/"
    titleresponse = requests.get(url)
    Soup = BeautifulSoup(titleresponse.text,'lxml')
    type_list = Soup.find('div', class_='menu-list').find_all('a')
    title_list = []
    title_urllist = []
    for info in type_list:
        title = info.get_text()  # 新闻分类
        title_href = info['href']
        title_url = url + title_href[1:]  # 新闻分类的url
        title_list.append(title)
        title_urllist.append(title_url)
    return title_list,title_urllist

