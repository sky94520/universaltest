#! /usr/bin/python3.6
# -*-coding:utf-8 -*-
"""
Item加载器，负责为item的字段提取值，并导出为item
"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChinaLoader(NewsLoader):
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())
