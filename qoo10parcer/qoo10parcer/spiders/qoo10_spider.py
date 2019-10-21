# -*- coding: utf-8 -*-
import scrapy


class Qoo10SpiderSpider(scrapy.Spider):
    name = 'qoo10'

    def start_requests(self):
        urls = [
            'https://www.qoo10.sg/s/EYELASH?keyword=eyelash&keyword_auto_change=',
            # 'https://www.qoo10.sg/s/?search_option=tt&gdlc_cd=&gdmc_cd=&gdsc_cd=&keyword_hist=eyelash&delivery_group_no=&bundle_policy=&bundle_delivery=&keyword=&sortType=RANK_POINT_FEMALE&dispType=LIST&flt_pri_idx=&filterDelivery=NNNNNANNNN&search_global_yn=&basis=&shipFromNation=&shipto=RU&brandnm=&SearchNationCode=&is_research_yn=Y&hid_keyword=eyelash&quick_delivery_yn=&qprime_yn=&shipping_avg_dt=&video_goods_yn=&coupon_filter_no=&gd_type=&drugs_type=&relation_group_no=&multiple_ship_from_yn=Y&priceMin=&priceMax=&category_specific_kw_nos=&curPage=2&pageSize=60&partial=off&brandno=#anchor_detail_top'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        for block in response.css('#search_result_item_list tr'):
            items.append({
                'description': block.css('a[data-type=goods_url]::attr(title)').get(),
                'image_link': block.css('a[data-type=goods_url] img::attr(src)').get(),
                'price': block.css('.prc strong::text').get(),
            })
        print('--- START CODE ---')
        print(items)
        print('--- END CODE ---')
