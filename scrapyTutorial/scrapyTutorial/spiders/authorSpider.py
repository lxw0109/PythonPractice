#!/usr/bin/env python3
# coding: utf-8
# File: authorSpider.py
# Author: lxw
# Date: 4/16/17 17:52 PM

import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('small.author + a::attr(href)').extract():
            yield scrapy.Request(url=response.urljoin(href), callback=self.parse_author)

        # follow pagination links
        next_link = response.css("li.next a::attr(href)").extract_first()
        if next_link:
            next_link = response.urljoin(next_link)
            yield scrapy.Request(url=next_link, callback=self.parse)

    def parse_author(self, response):
        def extract_with_CSS(query):
            return response.css(query).extract_first().strip()
        name = extract_with_CSS('h3.author-title::text')
        born_date = extract_with_CSS('span.author-born-date::text')
        bio = extract_with_CSS('div.author-description::text')
        yield dict(name=name, bornDate=born_date, bio=bio)

