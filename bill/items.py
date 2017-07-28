# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BillItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    artists = scrapy.Field()
    ranking = scrapy.Field()
    year = scrapy.Field()

    
class BillItemar(scrapy.Item):

	artists = scrapy.Field()
	ranking = scrapy.Field()
	year = scrapy.Field()

class BillItemall(scrapy.Item):

	name = scrapy.Field()
	ranking = scrapy.Field()
	
		