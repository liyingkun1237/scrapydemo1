# -*- coding: utf-8 -*-
"""
Created on Tue Aug 09 15:16:16 2016

@author: yingkun.li
"""

import scrapy
from qiubai.items import QiubaiItem

class QiuBaiSpider(scrapy.Spider):
    name = 'qiubai'
    start_urls = ['http://www.qiushibaike.com/']
    
    
    has_debug=False
    def parse(self, response):
        """#调试终端
        if not self.has_debug:
            from scrapy.shell import inspect_response
            inspect_response(response,self)
            self.has_debug=True
            """
      
        #提取糗百的笑话的作者和内容
        pattern1='//div[@class="article block untagged mb15"]'
        pattern2='./div[@class="author clearfix"]/a[2]/h2/text()'
        pattern3='./div[@class="content"]/text()'
        for ele in response.xpath(pattern1):
            authors=ele.xpath(pattern2).extract()
            contents=ele.xpath(pattern3).extract()
        
            yield QiubaiItem(author=authors,content=contents)
        