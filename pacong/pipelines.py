# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from pacong.items import MovieNews, MovieChina, MovieOuMei, MovieRiHan;


class PacongPipeline(object):

    movie = ['movie_new', 'movie_china', 'movie_oumei', 'movie_rihan']

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        self.tdb = client[dbName]
        # self.post = tdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        if isinstance(item, MovieNews):
            post = self.tdb[self.movie[0]]
            movieInfo = dict(item)
            post.insert(movieInfo)
        elif isinstance(item, MovieChina):
            post = self.tdb[self.movie[1]]
            movieInfo = dict(item)
            post.insert(movieInfo)
        elif isinstance(item, MovieOuMei):
            post = self.tdb[self.movie[2]]
            movieInfo = dict(item)
            post.insert(movieInfo)
        elif isinstance(item, MovieRiHan):
            post = self.tdb[self.movie[3]]
            movieInfo = dict(item)
            post.insert(movieInfo)
        return item
