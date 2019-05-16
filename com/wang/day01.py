#!/usr/bin/env python
def hello():
    print("hello,world")

    hello()

import pymongo
uri = "mongodb://sa:123@127.0.0.1:27017/?authSource=admin&authMechanism=SCRAM-SHA-256"
myclient = pymongo.MongoClient(uri)
dblist = myclient.list_database_names()
print([r for r in dblist])
#dblist = myclient.database_names()
if "hujin3_india_risk" in dblist:
     print("数据库已存在！")
db=myclient.hujin3_test_wang
collection=db['test']
rel=collection.find()
print([r for r in rel])
# rel=collection.find({"name":"Alex"})
# print([r for r in rel]) # rel=collection.find({"age":{"$gt":20}})
# # rel=collection.find({"$or":[{"name":"Amy"},{"name":"Alex"}]})
# print([r for r in rel])
# rel=collection.find_one({"name":"jack"})
# print(rel)
# print(rel['name'])#单个文档情况下可用来取出指定值

#插入多个文档
mylist = [
    { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
    { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
    { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
    { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
    { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]

x = collection.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)