# -*- coding: utf-8 -*-
import scrapy


class Qoo10SpiderSpider(scrapy.Spider):
    name = 'qoo10'
    query = input('Put search query: ')
    start_urls = [
        'https://www.qoo10.sg/s/' + query + '?keyword=' + query + '&keyword_auto_change=',
        'https://www.qoo10.sg/s/?search_option=tt&gdlc_cd=&gdmc_cd=&gdsc_cd=&keyword_hist=' + query +
        '&delivery_group_no=&bundle_policy=&bundle_delivery=&keyword=&sortType=RANK_POINT_FEMALE&dispType=LIST&flt'
        '_pri_idx=&filterDelivery=NNNNNANNNN&search_global_yn=&basis=&shipFromNation=&shipto=RU&brandnm=&SearchNation'
        'Code=&is_research_yn=Y&hid_keyword=' + query + '&quick_delivery_yn=&qprime_yn=&shipping_avg_dt=&video_goods_'
        'yn=&coupon_filter_no=&gd_type=&drugs_type=&relation_group_no=&multiple_ship_from_yn=Y&priceMin=&priceMax=&'
        'category_specific_kw_nos=&curPage=2&pageSize=60&partial=off&brandno=',
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
