import scrapy
import json
import math

city_url = 'https://www.graana.com/api/property/search?city_id={}&purpose=rent&type=residential&unit=marla&offset={}&page={}'

list_of_city_ids = [1] # Currently passing Islamabad only
class RealestateGraanaSpider(scrapy.Spider):
    name = 'realestate_graana'
    allowed_domains = ['graana.com']

    def start_requests(self):
        for city_id in list_of_city_ids:
            yield scrapy.Request(city_url.format(city_id,0,1),callback=self.parse_count,
            cb_kwargs=dict(city_id=city_id))

    def parse_count(self,response,city_id):
        raw_data = response.body
        data = json.loads(raw_data)
        prop_count = data["total"]
        page_size = 30

        #set offset and pagination
        no_of_pages = math.ceil(prop_count/page_size)
        #parse each page response
        for page_no in range(no_of_pages):
            offset = page_no
            page_no=page_no+1
            yield scrapy.Request(city_url.format(city_id,offset*page_size,page_no),callback=self.parse)

    #parse json response
    def parse(self,response):
        raw_data = response.body
        data = json.loads(raw_data)
        for item in data["items"]:
            yield {
            'Purpose':item['purpose'],
            'Type' : item['type'],
            'Price':item['price'],
            'SizeUnit': item['size_unit'],
            'Size':item['general_size'],
            'Bed':item['bed'],
            'Bath':item['bath'],
            'Phone': item['phone'],
            'Lat': item['lat'],
            'Lon': item['lon'],
            'City': item['city']['name'],
            'Area': item['area']['name'],
            "Url":  'https://www.graana.com/property/{}'.format(item['id'])
        }

        

