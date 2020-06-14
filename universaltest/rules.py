#! /usr/bin/python3.6
# -*-coding:utf-8 -*-
"""
提取规则存放，当callback为None时，默认跟进该页面
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china':
        (
            Rule(LinkExtractor(allow=r'article\/.*\.html',
                               restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item',
                 follow=True),
            # 下一页链接
            Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(., "下一页")]'))
        )
}
