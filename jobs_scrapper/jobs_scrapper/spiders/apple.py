import scrapy
from scrapy.crawler import CrawlerProcess
from time import sleep
import random

apple_url = 'https://jobs.apple.com'


class AppleSpider(scrapy.Spider):
    name = 'apple'
    start_urls = [
        'https://jobs.apple.com/en-us/search?sort=relevance&key=software&location=united-states-USA'
    ]

    def parse(self, response):
        for post in response.css('tbody'):
            yield {
                "Title": post.css("td.table-col-1 a::text").get(),
                "Category": post.css("td.table-col-1 span.table--advanced-search__role::text").get(),
                "Location": post.css("td.table-col-2 span::text").get(),
                "Date Posted": post.css("td.table-col-1 span.table--advanced-search__date::text").get(),
                "Url": apple_url + post.css("td.table-col-1 a").attrib['href'].get(),
            }

        # next_page = response.css('li.pagination__next a::attr(href)').get()
        # if next_page is not None:
        #     sleep(random.random(.2,1.2))
        #     yield response.follow(next_page, callback=self.parse)


# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'


def run_spider(spider_class, filename, file_format):
    process = CrawlerProcess({
        "FEEDS": {
            filename: {"format": f"{file_format}"},
        },
    })

    process.crawl(spider_class)
    process.start()


# run_spider(spider_class=AppleSpider, filename="apple.json", file_format='json')
