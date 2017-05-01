#!/usr/bin/env python3
# coding: utf-8
# File: itemPipelineSpider.py
# Author: lxw
# Date: 5/1/17 3:40 PM


import scrapy
from scrapyTutorial.items import JsonWriteItem


class ItemPipelineSpider(scrapy.Spider):
    name = "item_pipeline"

    start_urls = [
        "http://xiaoweiliu.cn/archives/",
    ]

    def parse(self, response):
        article_list = response.xpath('//li[@class="post-item"]')
        date_list = article_list.xpath('./div/time/text()').extract()
        title_list = article_list.xpath('./span/a/text()').extract()
        link_list = article_list.xpath('./span/a/@href').extract()
        for date, title, link in zip(date_list, title_list, link_list):
            jwi = JsonWriteItem()
            jwi["date"] = date
            jwi["title"] = title
            jwi["link"] = "http://xiaoweiliu.cn" + link
            yield jwi
