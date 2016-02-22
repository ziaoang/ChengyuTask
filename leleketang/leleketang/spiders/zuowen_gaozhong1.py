from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):
	name = 'zuowen_gaozhong1'
	allowed_domains = ['leleketang.com']
	start_urls = []

	def __init__(self):
		max_page = 2532
		for i in range(1, max_page+1):
			self.start_urls.append("http://www.leleketang.com/zuowen/list30-0-0-%d-1.shtml"%i)

	def parse(self, response):
		id = response.url.split("/")[-1].split("-")[3]
		a = response.xpath('//span[@class="list_anchor_title clearfix"]/a/@href').extract()
		df = open("data/urls_gaozhong.txt", 'a')
		df.write(id + '\t')
		df.write(' '.join(a) + '\n')
		df.close()
