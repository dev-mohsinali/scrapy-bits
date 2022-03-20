import scrapy
from itemloaders.processors import (TakeFirst,MapCompose)
from w3lib.html import remove_tags
from dateutil import parser
import re

def get_rating(value):
    return value[:3]
def get_date(value):
    date_string = re.findall(r"on(.*)", value)
    return parser.parse(''.join(map(str, date_string)).strip())
def get_country_region(value):
    country_region = re.findall(r"the(.*)on", value)
    return ''.join(map(str, country_region)).strip()

class ReviewItem(scrapy.Item):
    rating = scrapy.Field(
        input_processor=MapCompose(get_rating),
        output_processor=TakeFirst()
    )
    title = scrapy.Field(
        output_processor=TakeFirst()
    )
    date = scrapy.Field(
         input_processor=MapCompose(get_date),
        output_processor=TakeFirst()
    )
    country_region = scrapy.Field(
         input_processor=MapCompose(get_country_region),
        output_processor=TakeFirst()
    )
    
    review = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    page_url = scrapy.Field(
        output_processor=TakeFirst()
    )