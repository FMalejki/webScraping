# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CarsItems(scrapy.Item):
    price = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    #another info. if needed would be added

