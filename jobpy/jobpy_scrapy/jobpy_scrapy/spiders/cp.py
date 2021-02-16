# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest 


class CBSpider(scrapy.Spider):
    name = 'cb'
    allowed_domains = ['https://www.careerbuilder.com/jobs?keywords=python+developer&location=']
    start_urls = ['https://www.careerbuilder.com/jobs?keywords=python+developer&location=']

    def start_requests(self): 
        yield SeleniumRequest( 
            url ="https://www.careerbuilder.com/jobs?keywords=python+developer&location=",
            wait_time = 3, 
            screenshot = True, 
            callback = self.parse,  
            dont_filter = True,    
        ) 

    def parse(self, response):
        
        jobs = response.css('.job-listing-item')
   

        for job in jobs:
            job_title = job.css('.data-results-title::text').get()
            company = job.css('.data-details').css('span::text').get()
            location = job.css('.data-details').css('span:nth-child(2)::text').get()
            apply = job.css('.data-results-content').attrib['href']

            yield {
                "Job Title": job_title,
                "Company": company,
                "Location": location,
                "Apply": "https://www.careerbuilder.com" + apply,
            }
