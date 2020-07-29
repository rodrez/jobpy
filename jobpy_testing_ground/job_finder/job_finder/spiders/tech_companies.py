import scrapy


class TechCompaniesSpider(scrapy.Spider):
    name = 'tech_companies'
    start_urls = ['https://www.forbes.com/top-digital-companies/list/#tab:rank/']

    def start_requests(self):
        urls = [
            
            'https://www.forbes.com/top-digital-companies/list/#tab:rank/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.css('tbody'):
            yield {
                'Rank': post.css('tr.td.name::text').get().strip(),
                'Name': post.css('tr.td.rank::text').get().strip(),
            }