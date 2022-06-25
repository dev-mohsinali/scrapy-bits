# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter

import sqlite3


def tuple_to_custom_string(val):
    refined_list = re.findall(r"[^(),']", str(val))
    return ''.join(map(str, refined_list))


class RealestateGraanaListingsPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("graana_listings.db")
        self.cursor = self.connection.cursor()
        self.create_clean_table()

    def create_clean_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS "granna_listing_tbl" (
            "purpose"	TEXT,
            "type"	TEXT,
            "price"	INTEGER,
            "sizeunit"	TEXT,
            "size"	NUMERIC,
            "bed"	INTEGER,
            "bath"	INTEGER,
            "phone"	TEXT,
            "lat"	NUMERIC,
            "lon"	NUMERIC,
            "city"	TEXT,
            "area"	TEXT,
            "url"	TEXT
        )
        """)
        self.cursor.execute("DELETE from granna_listing_tbl")

    def process_item(self, item, spider):
        graana_item = [item['purpose'], item['type'], item['price'], item['size_unit'], item['general_size'],
                       item['bed'], item['bath'], item['phone'], ['lat'], item['lon'], item['city'],
                       item['area'], item['url']]
        # slicing string
        self.cursor.execute("""
            INSERT INTO granna_listing_tbl VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            [tuple_to_custom_string(item) for item in graana_item])
        self.connection.commit()
        return item
