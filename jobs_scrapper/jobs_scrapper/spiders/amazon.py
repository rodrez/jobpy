from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy_splash import SplashRequest


class AmazonSpider(Spider):
    name = 'amazon'
    page_number = 10
    start_urls = [
        'https://www.amazon.jobs/en/job_categories/software-development'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 3})

    def parse(self, response):
        for post in response.css('div.job'):
            yield {
                'Job': post.css('h3.job-title::text').get().strip(),
                'Location': post.css('p.location-and-id::text').get().strip(),
                'Date Posted': post.css('p.meta.time-elapsed::text').get().strip(),
            }
        #button.btn.circle.right

        next_page = f'https://www.amazon.jobs/en/job_categories/software-development?offset={str(AmazonSpider.page_number)}&result_limit=10&sort=relevant&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&'

        # TODO: Remove hard coded quantity and replace with dynamic entry
        last_page = str(response.css('div.pagination-control button:nth-child(6)::text').get())
        if AmazonSpider.page_number < 10:
            AmazonSpider.page_number += 10
            yield SplashRequest(url=next_page, callback=self.parse)


def run_spider(spider_class, filename, file_format):
    process = CrawlerProcess({
        "FEEDS": {
            filename: {"format": f"{file_format}"},
        },
    })
    process.crawl(spider_class)
    process.start()

# run_spider(spider_class=MySpider, filename='microsoft', file_format='json')