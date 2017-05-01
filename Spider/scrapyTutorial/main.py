#!/usr/bin/env python3
# coding: utf-8
# File: main.py
# Author: lxw
# Date: 4/21/17 2:31 PM

from scrapy import cmdline

# cmdline.execute(["scrapy", "crawl", "neeq", "-L", "WARNING"])
# cmdline.execute("scrapy crawl quotes -L WARNING".split())
# cmdline.execute("scrapy crawl selectors -L WARNING".split())
cmdline.execute("scrapy crawl item_pipeline -L WARNING".split())

