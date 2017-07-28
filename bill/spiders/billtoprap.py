from bill.items import BillItem
from scrapy import Spider, Request


class BillSpider(Spider):
	name = 'billtoprap_spider'
	allowed_ulrs = ['http://www.billboard.com/charts']
	start_urls = ['http://www.billboard.com/charts/year-end/' + str(i) + '/hot-rap-songs' for i in range(2006, 2017)] 



	def parse(self, response):
		year = response.xpath('.//div[@class="ye-chart__year-nav"]/text()').extract()[2].strip('\n')

		entries = response.xpath('.//*[@class="ye-chart__item-wrapper"]')

		ranking = response.xpath('//div[@class="ye-chart__item-rank"]/text()').extract()
		name = response.xpath('//h1[@class="ye-chart__item-title"]/text()').extract()
		artists = response.xpath('//*[@class="ye-chart__item-subtitle-link"]/text()').extract()
		year = response.xpath('.//div[@class="ye-chart__year-nav"]/text()').extract()[2].strip('\n')
		for i in range(0, len(ranking)):
			item = BillItem()
			item['ranking'] = ranking[i]
			item['name'] = name[i].strip('\n')
			item['artists'] = artists[i].strip('\n')
			item['year'] = year

			yield item

