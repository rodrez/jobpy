# -*- coding: utf-8 -*-
import scrapy


class SnagAJobSpider(scrapy.Spider):
    name = 'snag_a_job'
    allowed_domains = ['www.snagajob.com/search?q=software+engineer&w=17055&radius=50']
    start_urls = ['http://www.snagajob.com/search?q=software+engineer&w=17055&radius=50/']

    def parse(self, response):
        pass
