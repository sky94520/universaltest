# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from universaltest.utils import get_config
from universaltest.rules import rules
from universaltest.items import *
from universaltest.loaders import *
from universaltest import urls


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        # 获取爬取规则
        self.rules = rules.get(config.get('rules'))
        self.allowed_domains = config.get('allowed_domains')
        # 获取start_urls
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.%s' % start_urls.get('method'))(*start_urls.get('args', [])))
        print('将要爬取的页面链接')
        print(self.start_urls)

        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')

        if item:
            # 创建对应的Item和ItemLoader
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置 item[key] = ...
            for key, value in item.get('attrs').items():
                # 目前仅三种：分别为method args re
                for extractor in value:
                    # method：使用什么方法
                    method, args, r = extractor['method'], extractor['args'], extractor['re']
                    # 判断
                    if method == 'xpath':
                        loader.add_xpath(key, *args, **{'re': r})
                    elif method == 'css':
                        loader.add_css(key, *args, **{'re': r})
                    elif method == 'value':
                        loader.add_value(key, *args, **{'re': r})
                    elif method == 'attr':
                        loader.add_value(key, getattr(response, *args))
                # 返回Item
                yield loader.load_item()
