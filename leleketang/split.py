# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from collections import defaultdict

type = "xiaoxue"

POOL = set()
for line in open("statistic/%s.txt"%type):
	t = line.strip().split('\t')
	cy, cnt = t[0], int(t[1])
	if cnt >= 100:
		POOL.add(cy)

cy_paragraph = defaultdict(list)
for filename in os.listdir("data_filter_seg/%s"%type):
	print(filename)
	content = open("data_filter_seg/%s/%s"%(type, filename)).read()
	cy_list, zw_title, zw_content = content.strip().split("\n\n")
	same_pool = set()
	for cy in cy_list.strip().split(' '):
		if cy in POOL:
			same_pool.add(cy)
	for paragraph in zw_content.split('\n'):
		for cy in same_pool:
			if cy in paragraph.strip().split("/ "):
				cy_paragraph[cy].append(paragraph)


df_train = open("data_filter_seg_split/%s_train.txt"%type, 'w')
for cy in cy_paragraph:
	split_index = int(0.8 * len(cy_paragraph[cy]))
	df_train.write("%s\t%s\n"%(cy, '\t'.join(cy_paragraph[cy][:split_index])))
df_train.close()

df_test = open("data_filter_seg_split/%s_test.txt"%type, 'w')
for cy in cy_paragraph:
	split_index = int(0.8 * len(cy_paragraph[cy]))
	df_test.write("%s\t%s\n"%(cy, '\t'.join(cy_paragraph[cy][split_index:])))
df_test.close()