# encoding=utf-8
# import pymongo
#
# conn = pymongo.MongoClient()
# tdb = conn.aaaa
# post_info = tdb.test
# jike = {'name': 'aaa', 'age': '5'}
# post_1 = tdb.posts.insert_one(jike).inserted_id
# print post_1

class a:
    def __init__(self):
        print "b"

    def run(self):
        print 'run'

class b(a):

    def run(self):
        print "aaaa"

b = b()
b.run()

# def f(x):
#     return x*x
#
# list = map(lambda x :x +3, range(1,100))
#
# print list
