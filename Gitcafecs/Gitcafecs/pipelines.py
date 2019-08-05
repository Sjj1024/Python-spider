# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter

class GitcafecsPipeline(object):
    def open_spider(self, spider):
        self.file = open("weizhang.json", "a+", encoding="utf-8")
        self.file.write('[')

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item))
        self.file.write(json_str + ",\n")

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()
