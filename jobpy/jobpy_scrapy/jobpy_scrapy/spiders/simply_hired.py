# -*- coding: utf-8 -*-
import scrapy


class SimplyHiredSpider(scrapy.Spider):
    name = 'simply_hired'
    allowed_domains = ['www.simplyhired.com/search?q=software+engineer&l=usa&job=3dFGGBkCaunOJE2HHzyo3IUUt2hC1di2lDuu14jeW7ete4Gk4UVusw']
    start_urls = ['http://www.simplyhired.com/search?q=software+engineer&l=usa&job=3dFGGBkCaunOJE2HHzyo3IUUt2hC1di2lDuu14jeW7ete4Gk4UVusw/']

    def parse(self, response):
        pass
