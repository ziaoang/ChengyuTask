from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import os

class MininovaSpider(CrawlSpider):
	name = 'zuowen_chuzhong2'
	allowed_domains = ['leleketang.com']
	start_urls = []

	def __init__(self):
		pool = set()
		for filename in os.listdir("data/zuowen_chuzhong"):
			pool.add(filename)
		new = set()
		for line in open("data/urls_chuzhong.txt"):
			t = line.strip().split('\t')
			if len(t) != 2:
				continue
			for url in t[1].split(' '):
				new.add(url)
		for url in new - pool:
			self.start_urls.append("http://www.leleketang.com/zuowen/"+url)

	def parse(self, response):
		df = open("data/zuowen_chuzhong/"+response.url.split("/")[-1], 'w')
		df.write(response.body)
		df.close()
