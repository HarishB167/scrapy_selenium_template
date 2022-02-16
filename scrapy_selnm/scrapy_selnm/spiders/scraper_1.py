import scrapy

# Ref : https://github.com/clemfromspace/scrapy-selenium
# Ref : https://stackoverflow.com/questions/68870629/unable-to-run-scrapy-selenium-library-with-ui-with-head
# Ref : https://stackoverflow.com/questions/66157915/keyerror-driver-in-printresponse-request-metadriver-title
from scrapy_selenium import SeleniumRequest
from selenium.common.exceptions import NoSuchElementException 

import time

class ScraperTemplate(scrapy.Spider):
    name = "scraperTemplate"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # You can add this variable as meta parameter in next follow request in this function
        # Ref : https://stackoverflow.com/questions/55529949/scrapy-how-to-pass-an-item-between-methods-using-meta
        driver = response.request.meta['driver']
  
        for quote in response.css('div.quote'):
            result = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
            print(result)
            yield result

        
            