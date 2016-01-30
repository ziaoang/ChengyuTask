from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class MininovaSpider(CrawlSpider):
	name = 'yaoguo'
	start_urls = []

	def __init__(self):
		for i in range(100):
			self.start_urls.append("http://api.spark.appublisher.com/quizbank/get_note_questions?user_id=1146660&user_token=e837c7c710c258d605f108317ecfbc07&hierarchy_3=635&type=note")

	def parse(self, response):
		df = open("data.txt", 'a')
		df.write(response.body+"\n")
		df.close()
