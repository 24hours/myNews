# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
import re
import time 
import pymongo

class DupePipeline(object):
  def __init__(self):
    self.ids_seem = set()

  def process_item(self, item, spider):
    client = MongoClient()
    db = client['newsDatabase']
    coll = db['news']

    if item['url'] in self.ids_seen or coll.find_one(item['url']) is not None:
      raise DropItem("Duplicate item found: %s" % item)
    else:
      self.ids_seen.add(item['url'])
    return item


class DatePipeline(object):
  # normalized the date 
  def process_item(self, item, spider):
    if spider.name is 'rakyat':
      date = re.sub('PUBLISHED:', '', item['date']).strip()
      pdate = time.strptime(date, '%b %d, %Y %I:%M%p')
      item['date'] = time.strftime("%a, %d %b %Y %H:%M:%S +0000", pdate)
    elif spider.name is 'star':
      pass
    elif spider.name is 'insider':
      date = re.sub('Published:', '', item['date']).strip()
      pdate = time.strptime(date, '%d %b %Y %I:%M %p')
      item['date'] = time.strftime("%a, %d %b %Y %H:%M:%S +0000", pdate)

    return item

class ContentPipeline(object):
  def process_item(self, item, spider):
    news = re.sub( r'<.*?>', '', item['news'])
    news = re.sub( r'(\r|\n|\t)', '', news)
    item['news'] = news    
    # print news
    return item

class MongoPipeline(object):
  def process_item(self, item, spider):
    client = MongoClient()
    db = client['newsDatabase']
    item['_id'] = item['url']
    result = db.news.insert_one(dict(item))
