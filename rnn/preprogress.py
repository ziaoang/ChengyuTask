# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def loadStatistic():
	cy_cnt = {}
	for line in open("data/raw/all_statistic.txt"):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cy_cnt[cy] = cnt
	return cy_cnt

cy_cnt = loadStatistic()

def pre(t):
	res = []
	for cy in cy_cnt:
		if cy in t:
			cy_index = t.index(cy)
			res.append("/ ".join(t[:cy_index+1]))
	return res

def aft(t):
	t.reverse()
	return pre(t)

for kind in ["train", "test"]:
	df_pre = open("data/%s_pre.txt"%kind, 'w')
	df_aft = open("data/%s_aft.txt"%kind, 'w')
	for line in open("data/raw/all_%s.txt"%kind):
		t = line.strip().split("/ ")
		for content in pre(t):
			df_pre.write(content+'\n')
		for content in aft(t):
			df_aft.write(content+'\n')
	df_pre.close()
	df_aft.close()

