from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):
	name = 'zuowen_xiaoxue1'
	allowed_domains = ['leleketang.com']
	start_urls = []

	def __init__(self):
		pool = set()
		for line in open("data/urls_xiaoxue.txt"):
			t = line.strip().split('\t')
			if len(t) == 2:
				pool.add(int(t[0]))


		max_page = 16968
		for i in range(1, max_page+1):
			if i not in pool:
				self.start_urls.append("http://www.leleketang.com/zuowen/list10-0-0-%d-1.shtml"%i)

	def parse(self, response):
		id = response.url.split("/")[-1].split("-")[3]
		a = response.xpath('//span[@class="list_anchor_title clearfix"]/a/@href').extract()
		df = open("data/urls_xiaoxue.txt", 'a')
		df.write(id + '\t')
		df.write(' '.join(a) + '\n')
		df.close()
