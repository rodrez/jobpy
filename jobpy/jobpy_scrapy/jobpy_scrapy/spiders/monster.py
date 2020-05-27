# -*- coding: utf-8 -*-
from scrapy import Spider


class MonsterSpider(Spider):
    name = 'monster'
    allowed_domains = ['www.monster.com/jobs/search/?q=sofware-engineer&tm=14']
    start_urls = ['http://www.monster.com/jobs/search/?q=sofware-engineer&tm=14/']

    def parse(self, response):
        for post in response.css('div.summary'):
            yield {
                'Job': post.css('h2.title').get(),
                'Company': post.css('div.company span.name').get(),
                'Location': post.css('div.location span.name').get(),
                'Url': post.css('h2.title a::attr(href)').get(),
            }
