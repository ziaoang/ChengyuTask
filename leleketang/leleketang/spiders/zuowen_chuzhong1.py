from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):
	name = 'zuowen_chuzhong1'
	allowed_domains = ['leleketang.com']
	start_urls = []

	def __init__(self):
		max_page = 5475
		for i in range(1, max_page+1):
			self.start_urls.append("http://www.leleketang.com/zuowen/list20-0-0-%d-1.shtml"%i)

	def parse(self, response):
		id = response.url.split("/")[-1].split("-")[3]
		a = response.xpath('//span[@class="list_anchor_title clearfix"]/a/@href').extract()
		df = open("data/urls_chuzhong.txt", 'a')
		df.write(id + '\t')
		df.write(' '.join(a) + '\n')
		df.close()
