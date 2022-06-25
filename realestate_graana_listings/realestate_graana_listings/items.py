# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateGraanaListingsItem(scrapy.Item):
    # define the fields for your item here like:
    purpose = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    size_unit = scrapy.Field()
    general_size = scrapy.Field()
    bed = scrapy.Field()
    bath = scrapy.Field()
    phone = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    url = scrapy.Field()
