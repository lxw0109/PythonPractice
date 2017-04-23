#!/usr/bin/env python3
# coding: utf-8
# File: quotesSpider.py
# Author: lxw
# Date: 4/16/17 15:36 PM

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    """
    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1/",	
            "http://quotes.toscrape.com/page/2/",	
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    """
    start_urls = [
        "http://quotes.toscrape.com",
    ]

    def parse(self, response):
        print(type(response))   # <class 'scrapy.http.response.html.HtmlResponse'>
        for quote in response.css("div.quote"):
            content = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            yield dict(content=content, author=author, tags=tags)

        # next_link = response.css("li.next a::attr(href)").extract_first()
        # if next_link:
        #     next_link = response.urljoin(next_link)
        #     yield scrapy.Request(url=next_link, callback=self.parse)
