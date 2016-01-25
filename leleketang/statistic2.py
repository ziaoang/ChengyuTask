# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from collections import defaultdict

def loadUserDict():
	userdict = set()
	for line in open("../data/userdict.txt"):
		userdict.add(line.strip())
	return userdict

userdict = loadUserDict()

ALLWORD = defaultdict(int)
for line in open("data_filter_seg_merge/all.txt"):
	t = line.strip().split("/ ")
	for word in t:
		ALLWORD[word] += 1

COUNT_DICT = {}
for word in ALLWORD:
	if word in userdict:
		COUNT_DICT[word] = ALLWORD[word]

COUNT_LIST = [[key, COUNT_DICT[key]] for key in COUNT_DICT]
COUNT_LIST.sort(key=lambda a:a[1], reverse=True)
df = open("statistic/all.txt", 'w')
for t in COUNT_LIST:
	df.write("%s\t%s\n"%(t[0], t[1]))
df.close()