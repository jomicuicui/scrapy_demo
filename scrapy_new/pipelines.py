# -*- coding: utf-8 -*-

import pymysql
from scrapy_new import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




from scrapy.exceptions import DropItem


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
#
#     def __init__(self):
#         self.score = 8.5
#
#     def process_item(self, item, spider):
#         # if item['score']:
#         #     if float(item['score']) <= float(self.score):
#         #         item.remove(item['score'])
#             return item
#         # else:
#         #     return DropItem('Missing Score')
class MysqlPipeline(object):
    def __init__(self):
        #链接数据库
        self.connect = pymysql.connect(
            host=settings.mysql_host,    #数据库地址
            database=settings.mysql_database,  #数据库库名
            user=settings.mysql_user,  #数据库用户名
            password=settings.mysql_password,   #数据库密码
            port=settings.mysql_port,   #数据库端口
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor)
        #通过cursor执行增删改查
        self.cursor = self.connect.cursor()

    def close_spider(self,spider):
        self.cursor.close()

    def process_item(self,item,spider):
        # print(item)
        try:
            #去重处理
            self.cursor.execute(
                "select * from clws where title_url = %s",item['message_url']
            )
            #是否有重复数据
            repetition = self.cursor.fetchone()
            #重复
            if repetition:
                pass
            else:
                sql = 'insert into clws(title,title_url,headlineinfo,message_title,message_url) VALUES (%s,%s,%s,%s,%s)'    #向表中插入数据
                # print(item)   #打印前面返回的item
                # lis=tuple((item['title'],item['title_url']),)
                # print("=============>"+lis)
                self.cursor.execute(sql,(item['title'],item['title_url'],item['headlineinfo'],item['message_title'],item['message_url']))
                self.connect.commit()
        except Exception as error:
            print(error)
        return item    #必须实现返回

