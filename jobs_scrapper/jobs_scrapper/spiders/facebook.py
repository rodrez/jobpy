# -*- coding: utf-8 -*-
from random import random
from time import sleep

from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


class FacebokSpider(Spider):
    name = 'facebook'
    start_urls = [
        'https://www.facebook.com/careers/jobs/?divisions%5B0%5D=Facebook&is_leadership=0&is_in_page=0'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 4})

    def parse(self, response):
        for post in response.css('li.jobs-list-item'):

            yield {
                'Job': post.css('span.job-title::text').get().strip(),
                'Location': post.css('span.job-location::text').get().strip(),
                'Date Posted': post.css('span.job-date::text').get().strip(),
                'Url': post.css('div.job-title a::attr(href)'),
            }
        # FIXME follow the next items
        # next_page = response.css('ul.pagination').xpath('.//li[12]').css('a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


def run_spider(spider_class, filename, file_format):
    process = CrawlerProcess({
        "FEEDS": {
            filename: {"format": f"{file_format}"},
        },
    })
    process.crawl(spider_class)

# run_spider(spider_class=MicrosoftSpider, filename='microsoft', file_format='json')
# sudo docker run -p 8050:8050 scrapinghub/splash