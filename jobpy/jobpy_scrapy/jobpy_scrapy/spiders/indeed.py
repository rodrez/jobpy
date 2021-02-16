import scrapy
from scrapy_selenium import SeleniumRequest 


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['https://www.indeed.com/jobs?q=software+engineer&l=Mechanicsburg%2C+PA']
    start_urls = ['http://https://www.indeed.com/jobs?q=software+engineer&l=Mechanicsburg%2C+PA/']

    def start_requests(self): 
        yield SeleniumRequest( 
            url ='https://www.indeed.com/jobs?q=software+engineer&l=Mechanicsburg%2C+PA&sort=date', 
            wait_time = 3, 
            screenshot = True, 
            callback = self.parse,  
            dont_filter = True    
        ) 

    def parse(self, response):
        
        jobs = response.css('.jobsearch-SerpJobCard')
   

        for job in jobs:
            title = job.css('.jobtitle').attrib['title']
            company = job.css('.company').css('a::text').get()
            location = job.css('.location::text').get()
            apply_link = job.css('.jobtitle').attrib['href']


            yield {
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Apply": "https://www.indeed.com" + apply_link,
            }
