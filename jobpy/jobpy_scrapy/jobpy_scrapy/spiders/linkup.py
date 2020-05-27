# -*- coding: utf-8 -*-
import scrapy


class LinkupSpider(scrapy.Spider):
    name = 'linkup'
    allowed_domains = ['www.linkup.com/search/results/Software-Engineer-jobs-in-PA']
    start_urls = ['http://www.linkup.com/search/results/Software-Engineer-jobs-in-PA/']

    def parse(self, response):
        pass
