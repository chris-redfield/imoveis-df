import scrapy
import time 
from os import walk
import json
import datetime


class PropertySpider(scrapy.Spider):
    name = "property"

    def start_requests(self):
        urls = []
        for url in urls:
            time.sleep(1.5)
            yield scrapy.Request(url=url, callback=self.parse_property)
    
    def parse_property(self, response):
        property_dict = {
            "raw_data": response.css('body')
        }
        
        with open('./files/properties/properties.jsonl', 'a') as file:
            json.dump(property_dict, file)
            file.write('\n')
        
