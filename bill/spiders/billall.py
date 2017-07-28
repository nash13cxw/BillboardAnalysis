from bill.items import BillItemall
from scrapy import Spider, Request


class BillSpider(Spider):
	name = 'billtopall_spider'
	allowed_ulrs = ['http://www.billboard.com/charts']
	start_urls = ['http://www.billboard.com/charts/greatest-hot-100-artists']



	def parse(self, response):
		ranking = response.xpath('//span[@class="chart-row__current-week"]/text()').extract()
		name = response.xpath('//h2[@class="chart-row__song"]/text()').extract()
		
		for i in range(0, 101):
			item = BillItemall()
			item['ranking'] = ranking[i]
			item['name'] = name[i].strip('\n')

			yield item

