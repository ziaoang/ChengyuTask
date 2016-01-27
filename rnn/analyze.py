# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from collections import defaultdict

def loadStatistic():
	cy_cnt = {}
	for line in open("data/all_statistic.txt"):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cy_cnt[cy] = cnt
	return cy_cnt


def fenju(paragraph):
	t = paragraph.strip().split("/ ")
	res = []
	tmp = []
	for w in t:
		tmp.append(w)
		if w in ['。', '？', '！', '；', '.', '?', '!', ';']:
			res.append(tmp)
			tmp = []
	if len(tmp) > 0:
		res.append(tmp)
	return res

max_length = 0
max_pre_length = 0
max_after_length = 0

cy_cnt = loadStatistic()

pre = defaultdict(int)
after = defaultdict(int)

for line in open("data/all_train_small.txt"):
	t = line.strip().split("/ ")
	max_length = max(max_length, len(t))
	for cy in cy_cnt:
		if cy in t:
			cy_index = t.index(cy)
			max_pre_length = max(max_pre_length, cy_index)
			max_after_length = max(max_after_length, len(t)-1-cy_index)

			if cy_index <= 100:
				pre["<=100"] += 1
			else:
				pre[">100"] += 1

			if len(t)-1-cy_index <= 100:
				after["<=100"] += 1
			else:
				after[">100"] += 1

print(max_length)
print(max_pre_length)
print(max_after_length)

print(pre["<=100"])
print(pre[">100"])
print(after["<=100"])
print(after[">100"])


