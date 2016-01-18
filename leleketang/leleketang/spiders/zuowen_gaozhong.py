from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):
	name = 'zuowen_gaozhong'
	allowed_domains = ['leleketang.com']
	start_urls = []

	def __init__(self):
		max_page = 1
		max_page = 2532
		for i in range(1, max_page+1):
			self.start_urls.append("http://www.leleketang.com/zuowen/list30-0-0-%d-1.shtml"%i)
		#self.start_urls.append("http://www.leleketang.com/zuowen/list30-0-0-1-1.shtml")

	def parse(self, response):
		id = response.url.split("/")[-1].split("-")[3]
		df = open("data/urls_gaozhong.txt", "a")
		df.write("# %s page\n"%id)
		a = response.xpath('//a[@class="list_rating_5 ellipsis"]/@href').extract()
		for t in a:
			df.write(t+"\n")
		df.close()
