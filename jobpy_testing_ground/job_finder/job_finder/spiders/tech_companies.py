import scrapy
from scrapy_splash import SplashRequest


class TechCompaniesSpider(scrapy.Spider):
    name = 'tech_companies'
    start_urls = ['https://www.forbes.com/top-digital-companies/list/#tab:rank/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 3})

    def parse(self, response):
        for post in response.css('tbody'):
            yield {
                'Rank': post.css('tr.td.name::text').get().strip(),
                'Name': post.css('tr.td.rank::text').get().strip(),
            }