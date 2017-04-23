#!/usr/bin/env python3
# coding: utf-8
# File: selectors_demo.py
# Author: lxw
# Date: 4/21/17 3:01 PM

import scrapy


class SelectorsDemo(scrapy.Spider):
    name = "selectors"

    start_urls = ["http://doc.scrapy.org/en/latest/_static/selectors-sample1.html"]

    def parse(self, response):
        """
        <html>
         <head>
          <base href='http://example.com/' />
          <title>Example website</title>
         </head>
         <body>
          <div id='images'>
           <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
           <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
           <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
           <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
           <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
          </div>
         </body>
        </html>
        """
        print(response.body)

        print("--" * 30)
        # 1. css & xpath selectors
        print(response.xpath("//base/@href").extract())
        print(response.css("base::attr(href)").extract())

        # print(response.xpath("//a/@href").extract())
        print(response.xpath('//a[contains(@href, "image")]/@href').extract())
        # print(response.css("a::attr(href)").extract())
        print(response.css("a[href*=image]::attr(href)").extract())

        print(response.xpath('//a[contains(@href, "image")]/img/@src').extract())
        print(response.css('a[href*=image] img::attr(src)').extract())

        print("--" * 30)
        # 2. Nesting selectors
        links = response.xpath('//a[contains(@href, "image")]')
        print(links)
        for index, link in enumerate(links):
            # args = index, link.xpath('@href').extract_first(), link.css("img::attr(src)").extract_first()
            args = index, link.xpath('@href').extract_first(), link.xpath("img/@src").extract_first()
            # print(type(args))    # tuple
            print("Link number {0} points to url {1} and image {2}".format(*args))

        print("--" * 30)
        # 3. re
        print(response.xpath('//a[contains(@href, "image")]/text()').re(r"Name:\s*(.*) "))
        print(response.xpath('//a[contains(@href, "image")]/text()').re_first(r"Name:\s*(.*) "))

        print("--" * 30)
        # 4. relative XPaths(important)
        body = """
            <html>
                <head>
                    <base href='http://example.com/' />
                    <title>Example website</title>
                    <a href='image0.html'>Name: My image 0 <br /><img src='image0_thumb.jpg' /></a>
                </head>
                <body>
                    <div id='images'>
                        <img src='image6_thumb.jpg' />
                        <img src='image7_thumb.jpg' />
                        <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
                        <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
                        <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
                        <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
                        <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
                        <img src='image8_thumb.jpg' />
                        <img src='image9_thumb.jpg' />
                    </div>
                </body>
            </html>
            """
        sel = scrapy.selector.Selector(text=body, type="html")
        divs = sel.xpath("//div")
        for a_tag in divs.xpath("//a"):     # NO: extracts all <a> elements from the document, not only those inside <div> elements
            # 注意即使这里使用的是divs.xpath,提取的仍然是整个文档中的a标签
            # 串起来的Selector, 后面的XPath如果使用双斜杠一定要加"."
            print(a_tag.extract())

        print("--" * 10)
        for a_tag in divs.xpath(".//a"):     # YES: extracts only the <a> elements inside <div> elements
            print(a_tag.extract())

        print("--" * 10)
        # "extract all **direct** <img> children in div"
        # for direct_img in divs.xpath("./img/@src"):  # OK
        for direct_img in divs.xpath("img/@src"):  # OK
            print(direct_img.extract())

        print("--" * 30)
        # 5. Variables in XPath expressions
        print(response.xpath('//div[@id=$val]/a/text()', val="images").extract())
        print(response.xpath('//div[count(a)=$cnt]/a/text()', cnt=5).extract())
        print(response.xpath('//div[count(a)=$cnt]/@id', cnt=5).extract())

        sel = scrapy.selector.Selector(text='<time datetime="123"> <div class="hero shout"><time datetime="2014-07-23 19:00">Special date</time></div>', type="html")
        print(sel.css(".hero").xpath('./time/@datetime').extract())     # ['2014-07-23 19:00']
        print(sel.css(".shout").xpath('time/@datetime').extract())  # ['2014-07-23 19:00']
        print(sel.css(".hero shout").xpath('time/@datetime').extract())     # []    # NOTE
