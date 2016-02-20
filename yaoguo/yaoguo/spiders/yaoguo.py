from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scrapy.http import Request
from scrapy.http import FormRequest

import json

class MininovaSpider(CrawlSpider):
	name = 'yaoguo'
	start_urls = []

	def __init__(self):
		for i in range(1000):
			self.start_urls.append("http://api.spark.appublisher.com/quizbank/get_note_questions?terminal_type=iOS_phone&app_type=quizbank&app_version=2.4.0&uuid=8CE233A9-D6C9-47C7-931D-14D7D2AA702B&user_id=1146660&user_token=e837c7c710c258d605f108317ecfbc07&timestamp=1454683069.978049&idfa=CB049838-06EA-418E-B4FD-893E052F2151&hierarchy_1=1461&hierarchy_2=103&hierarchy_3=635&type=note")

	def parse(self, response):
		# df = open("data.txt", 'a')
		# df.write(response.body+"\n")
		# df.close()

		t = json.loads(response.body.strip())
		paper_id = str(t["paper_id"])
		questions = []
		for i in range(15):
			id = t["questions"][i]["id"]
			answer = t["questions"][i]["answer"]
			note_id = t["questions"][i]["note_id"]
			tmp = '{"answer":"%s","category":5,"id":%s,"is_right":true,"duration":1,"note_id":%d}'%(answer, id, note_id)
			questions.append(tmp)
		questions = '[' + ','.join(questions) + ']'
		
