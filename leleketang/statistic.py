# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from bs4 import BeautifulSoup
from collections import defaultdict


type = "gaozhong"

COUNT_DICT = defaultdict(int)
for filename in os.listdir("data_filter_seg/%s"%type):
	print(filename)
	content = open("data_filter_seg/%s/%s"%(type, filename)).read()
	cy_list, zw_title, zw_content = content.strip().split("\n\n")
	for paragraph in zw_content.strip().split('\n'):
		for cy in cy_list.strip().split(' '):
			if cy in paragraph.strip().split("/ "):
				COUNT_DICT[cy] += 1

COUNT_LIST = [[key, COUNT_DICT[key]] for key in COUNT_DICT]
COUNT_LIST.sort(key=lambda a:a[1], reverse=True)
df = open("statistic/%s.txt"%type, 'w')
for t in COUNT_LIST:
	df.write("%s\t%s\n"%(t[0], t[1]))
df.close()


