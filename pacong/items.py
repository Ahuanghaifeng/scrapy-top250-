# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class PacongItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    movieInfo = Field()
    star = Field()
    quote = Field()

class ZhiHuItem(Item):
    name = Field()
    followers = Field()
    follows = Field()
    headUrl = Field()

class ZhihuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()  #保存抓取问题的url
    title = Field()  #抓取问题的标题
    description = Field()  #抓取问题的描述
    answer = Field()  #抓取问题的答案
    name = Field()  #个人用户的名称

#最新电影
class MovieNews(Item):
    movie_name = Field() #电影名字
    movie_time = Field() #收录时间
    movie_image = Field() #电影图片
    movie_abstract = Field() #电影简介
    movie_download = Field() #电影下载地址

#经典电影
class MovieJd(Item):
    movie_name = Field() #电影名字
    movie_time = Field() #收录时间
    movie_image = Field() #电影图片
    movie_abstract = Field() #电影简介
    movie_download = Field() #电影下载地址

#中国电影
class MovieChina(Item):
    movie_name = Field()  # 电影名字
    movie_time = Field()  # 收录时间
    movie_image = Field()  # 电影图片
    movie_abstract = Field()  # 电影简介
    movie_download = Field()  # 电影下载地址

#欧美电影
class MovieOuMei(Item):
    movie_name = Field()  # 电影名字
    movie_time = Field()  # 收录时间
    movie_image = Field()  # 电影图片
    movie_abstract = Field()  # 电影简介
    movie_download = Field()  # 电影下载地址

#日韩电影
class MovieRiHan(Item):
    movie_name = Field()  # 电影名字
    movie_time = Field()  # 收录时间
    movie_image = Field()  # 电影图片
    movie_abstract = Field()  # 电影简介
    movie_download = Field()  # 电影下载地址
