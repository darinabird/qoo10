# -*- coding: utf-8 -*-
import scrapy


class Qoo10SpiderSpider(scrapy.Spider):
    name = 'qoo10'
    query = input('Put search query: ')
    start_urls = [
        'https://www.qoo10.sg/s/' + query + '?keyword=' + query + '&keyword_auto_change=',
        'https://www.qoo10.sg/gmkt.inc/Search/SearchAjaxAppend.aspx?search_type=SearchQooBoRecommendItems'
        '&search_keyword=' + query + '&shipto=RU&___cache_expire___=1571824461283',
    ]


    def parse(self, response):
        if response.css('#search_result_item_list tr'):
            for block in response.css('#search_result_item_list tr'):
                yield {
                        'description': block.css('a[data-type=goods_url]::attr(title)').get(),
                        'image_link': block.css('a[data-type=goods_url] img::attr(src)').get(),
                        'price': block.css('.prc strong::text').get(),
                    }
                continue

        elif response.css('.slide'):
            for block in response.css('.slide'):
                yield{
                    'description': block.css('.tt::text').get(),
                    'image_link': block.css('.thmb img::text').get(),
                    'price': block.css('.prc strong::text').get(),
                }
