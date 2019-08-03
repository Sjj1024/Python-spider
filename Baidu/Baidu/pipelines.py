# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from Baidu.items import GuokrdetailItem, GuokrItem


class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item

class GuokrPipeline(object):
    def open_spider(self, spider):
        self.file = open("guoke.json", "a+", encoding="utf-8")

    def process_item(self, item, spider):
        if isinstance(item, GuokrItem):
            print(dict(item))
            json_str = json.dumps(dict(item), ensure_ascii=False)
            self.file.write(json_str + "\n")
            return item

    def close_spider(self, spider):
        self.file.close()

class GuokrDetailPipeline(object):
    def open_spider(self,spider):
        self.file = open('guokrdetail.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item,GuokrdetailItem):
            print(item)
            json_str = json.dumps(dict(item),ensure_ascii=False)
            self.file.write(json_str+'\n')
        return item

    def close_spider(self,spider):
        self.file.close()
