# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import math
import jieba
from collections import defaultdict
from gensim.models import Word2Vec

question_filename = "../data/cy_question/data.txt"

f = {}
for line in open("data/cnt.txt"):
	t = line.strip().split("\t")
	f[t[0]] = int(t[1])

total = 0
right = 0

sf = open(question_filename)
while(1):
	line = sf.readline()
	if not line:
		break
	q_raw = sf.readline().strip()
	a = sf.readline().strip()
	b = sf.readline().strip()
	c = sf.readline().strip()
	d = sf.readline().strip()
	answer = sf.readline().strip()
	sf.readline()
	sf.readline()
	
	t = []
	t.append(["A", f[a]])
	t.append(["B", f[b]])
	t.append(["C", f[c]])
	t.append(["D", f[d]])
	t.sort(key=lambda x:x[1], reverse=True)
	
	total += 1
	if answer == t[0][0]:
		right += 1

print("%d/%d\t%.4f"%(right, total, right/float(total)))
