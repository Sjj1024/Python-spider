# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter


class GitcafecsPipeline(object):
    def open_spider(self, spider):
        self.file = open("weizhang.json", "wb")
        self.writer = JsonItemExporter(self.file)
        self.writer.start_exporting()

    def process_item(self, item, spider):
        # json_str = json.dumps(dict(item))
        # self.file.write(json_str + "\n")
        self.writer.export_item(item)
        return item

    def close_spider(self, spider):
        self.writer.finish_exporting()
        self.file.close()
