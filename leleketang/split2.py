# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from collections import defaultdict


POOL = {}
NOW = {}
for line in open("statistic/all.txt"):
	t = line.strip().split('\t')
	cy, cnt = t[0], int(t[1])
	if cnt >= 1000:
		POOL[cy] = cnt
		NOW[cy] = 0

df_train = open("data_filter_seg_merge_split/all_train.txt", 'w')
df_test = open("data_filter_seg_merge_split/all_test.txt", 'w')

lineNo = 0
for line in open("data_filter_seg_merge/all.txt"):
	lineNo += 1
	if lineNo % 100000 == 0:
		print(lineNo)
	t = line.strip().split("/ ")
	cnt = defaultdict(int)
	for word in t:
		if word in POOL:
			cnt[word] += 1
	if len(cnt) == 0:
		df_train.write(line.strip()+'\n')
		continue
	isEnough = True
	for word in cnt:
		if NOW[word] > 0.8 * POOL[word]:
			isEnough = False
			break
	if isEnough:
		df_test.write(line.strip()+'\n')
	else:
		df_train.write(line.strip()+'\n')
	for word in cnt: # update NOW dict
		NOW[word] += cnt[word]

df_train.close()
df_test.close()



