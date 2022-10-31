import scrapy
import time

class PagesSpider(scrapy.Spider):
    name = "pages"
    BASE_URL = "https://wimoveis.com.br"
    def start_requests(self):
        urls = []
        for url in urls:
            time.sleep(1.5)
            yield scrapy.Request(url=url, callback=self.parse_pages)
    
    def parse_pages(self, response):
        url_string = response.url

        filename = f'./files/filtered_pages/' + self.url_to_filename(url_string) + '.txt'

        with open(filename, 'a') as f:
            #TODO: add right response css
            properties_links = response.css('div[title=Properties] a::attr(href)').getall()

            for links in properties_links:
                self.BASE_URL + links
                f.write(self.BASE_URL + links + '\n')

        #TODO: add css address for the next button
        next_page = response.css('a[data-testid="next-btn"]::attr("href")').get()

        if next_page is not None:
            time.sleep(1.5)
            yield response.follow(next_page, self.parse_pages)
    