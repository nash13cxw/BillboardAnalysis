from bill.items import BillItem
from scrapy import Spider, Request


class BillSpider(Spider):
	name = 'billtopedm_spider'
	allowed_ulrs = ['http://www.billboard.com/charts']
	start_urls = ['http://www.billboard.com/charts/year-end/' + str(i) + '/hot-dance-electronic--songs' for i in range(2014, 2017)] + ['http://www.billboard.com/charts/year-end/2013/dance-electronic-songs']



	def parse(self, response):
		year = response.xpath('.//div[@class="ye-chart__year-nav"]/text()').extract()[2].strip('\n')

		entries = response.xpath('.//*[@class="ye-chart__item-wrapper"]')

		for entry in entries:
			name = entry.xpath('.//h1[@class="ye-chart__item-title"]/text()').extract_first()
			ranking = entry.xpath('.//div[@class="ye-chart__item-rank"]/text()').extract_first()

			if entry.xpath('.//*[@class="ye-chart__item-subtitle-link"]/text()').extract_first() is not None:
				artist = entry.xpath('.//*[@class="ye-chart__item-subtitle-link"]/text()').extract_first()
			else: 
				artist = entry.xpath('.//h1[@class="ye-chart__item-title"]/following-sibling::h2/text()').extract_first()


			item = BillItem()
			item['ranking'] = ranking
			item['name'] = name.strip('\n')
			item['artists'] = artist.strip('\n')
			item['year'] = year

			yield item

		entries = response.xpath('.//*[@class="ye-chart__item"]')

		for entry in entries:
			name = entry.xpath('.//h1[@class="ye-chart__item-title"]/text()').extract_first()
			ranking = entry.xpath('.//div[@class="ye-chart__item-rank"]/text()').extract_first()

			if entry.xpath('.//*[@class="ye-chart__item-subtitle-link"]/text()').extract_first() is not None:
				artist = entry.xpath('.//*[@class="ye-chart__item-subtitle-link"]/text()').extract_first()
			else: 
				artist = entry.xpath('.//h1[@class="ye-chart__item-title"]/following-sibling::h2/text()').extract_first()


			item = BillItem()
			item['ranking'] = ranking
			item['name'] = name.strip('\n')
			item['artists'] = artist.strip('\n')
			item['year'] = year

			yield item
