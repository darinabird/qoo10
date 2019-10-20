# -*- coding: utf-8 -*-
import scrapy

# from qoo10_parcer.qoo10_parcer import items
from ..items import Qoo10ParcerItem


class Qoo10SpiderSpider(scrapy.Spider):
    name = 'qoo10'
    # allowed_domains = ['qoo10.sg']
    start_urls = [
        'https://www.qoo10.sg/s/TROUSERS?keyword=trousers&keyword_auto_change='
    ]

    def parse(self, response):
        items = Qoo10ParcerItem()

        image_link = response.css('#plus_item_list img::attr(src)').extract()
        description = response.css('.sbj a').css('::txt').extract()
        price = response.css('#search_rst_gform strong::txt').extract()

        items['image_link'] = image_link
        items['description'] = description
        items['price'] = price

        yield items
