# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['www.indeed.com/jobs?q=software+engineer+intern&l=United+States']
    start_urls = ['http://www.indeed.com/jobs?q=software+engineer+intern&l=United+States/']

    def parse(self, response):
        pass
