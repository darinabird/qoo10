# -*- coding: utf-8 -*-
import scrapy


class Qoo10SpiderSpider(scrapy.Spider):
    name = 'qoo10'
    query = input('Put search query: ')
    page_num = 2  # input('Put page number: ')

    start_urls = [
        'https://www.qoo10.sg/s/' + query + '?keyword=' + query + '&keyword_auto_change=&curPage=1',
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

        for block in response.css('#search_result_item_list'):
            yield{
                'description': block.css('.sbj a::text').get(),
                'image_link': block.css('.thmb img::text').get(),
                'price': block.css('#search_result_item_list img::text').get(),
            }

        next_page = 'https://www.qoo10.sg/s/' + Qoo10SpiderSpider.query + '?keyword=' + Qoo10SpiderSpider.query\
                    + '&keyword_auto_change=&curPage=' + str(Qoo10SpiderSpider.page_num) + ''
        if Qoo10SpiderSpider.page_num < 10:
            Qoo10SpiderSpider.page_num += 1
            yield scrapy.Request(next_page, callback=self.parse)
