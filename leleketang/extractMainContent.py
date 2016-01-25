# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from bs4 import BeautifulSoup


def loadUserDict():
	userdict = set()
	for line in open("../userdict.txt"):
		userdict.add(line.strip())
	return userdict

def extractTitleAndContent(html):
	soup = BeautifulSoup(html)
	zw_title = soup.find("h2", "cp_htitle").get_text().strip()
	zw_content = ""
	for p in soup.find("div", "cp_content").find_all('p'):
		c = p.get_text().strip()
		if len(c) > 0:
			zw_content += p.get_text().strip() + '\n'
	return zw_title, zw_content


pool = set()
for filename in os.listdir("data_filter/xiaoxue"):
	pool.add(filename.split('.')[0])


userdict = loadUserDict()
for filename in os.listdir("data/zuowen_xiaoxue"):
	if filename.split('.')[0] in pool:
		continue
	print(filename)
	html = open("data/zuowen_xiaoxue/" + filename).read()
	zw_title, zw_content = extractTitleAndContent(html)
	match = []
	for cy in userdict:
		if cy in zw_content:
			match.append(cy)
	if len(match) > 0:
		id = filename.split('.')[0]
		df = open("data_filter/xiaoxue/%s.txt"%id, 'w')
		df.write(' '.join(match) + "\n\n")
		df.write(zw_title + "\n\n")
		df.write(zw_content)