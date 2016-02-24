# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from bs4 import BeautifulSoup



def extractTitleAndContent(html):
	soup = BeautifulSoup(html)
	zw_title = soup.find("h2", "cp_htitle").get_text().strip()
	zw_content = ""
	for p in soup.find("div", "cp_content").find_all('p'):
		c = p.get_text().strip()
		if len(c) > 0:
			zw_content += p.get_text().strip() + '\n'
	return zw_title, zw_content


for filename in os.listdir("data/zuowen_gaozhong"):
	print(filename)
	html = open("data/zuowen_gaozhong/" + filename).read()
	zw_title, zw_content = extractTitleAndContent(html)
	id = filename.split('.')[0]
	df = open("LeLeKeTangZuoWen/gaozhong/%s.txt"%id, 'w')
	df.write(zw_title.strip() + "\n")
	df.write(zw_content.strip() + "\n")
	df.close()