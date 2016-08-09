# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 15:16:16 2016

@author: yingkun.li
"""

import scrapy

class QiuBaiSpider(scrapy.Spider):
    name = 'qiubai'
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        print response.xpath('//div[@class="author clearfix"]').extract()
        