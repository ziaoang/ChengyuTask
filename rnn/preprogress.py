# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def loadStatistic():
	cy_cnt = {}
	for line in open("data/all_statistic.txt"):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cy_cnt[cy] = cnt
	return cy_cnt

cy_cnt = loadStatistic()

df = open("data/pre_train.txt", 'w')
for line in open("data/all_train_small.txt"):
	t = line.strip().split("/ ")
	for cy in cy_cnt:
		if cy in t:
			cy_index = t.index(cy)
			df.write("%s\n"%("/ ".join(t[:cy_index+1])))
df.close()

df = open("data/pre_test.txt", 'w')
for line in open("data/all_test.txt"):
	t = line.strip().split("/ ")
	for cy in cy_cnt:
		if cy in t:
			cy_index = t.index(cy)
			df.write("%s\n"%("/ ".join(t[:cy_index+1])))
df.close()