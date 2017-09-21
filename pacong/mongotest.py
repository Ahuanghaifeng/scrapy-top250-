# encoding=utf-8
import pymongo

conn = pymongo.MongoClient()
tdb = conn.aaaa
post_info = tdb.test
jike = {'name': 'aaa', 'age': '5'}
post_1 = tdb.posts.insert_one(jike).inserted_id
print post_1
