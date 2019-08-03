# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class BaiduPipeline(object):
    def process_item(self, item, spider):
        # print(11111111111111111111111)
        # print(item)
        return item

class GuokrPipeline(object):
    def open_spider(self, spider):
        self.file = open("guoke.json", "a+", encoding="utf-8")

    def process_item(self, item, spider):
        # print(11111111111111111111111)
        print(dict(item))
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str + "\n")
        return item

    def close_spider(self, spider):
        self.file.close()
