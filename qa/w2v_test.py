# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import math
import jieba
from collections import defaultdict
from gensim.models import Word2Vec

sg = 1
cos = 0
window = 5
size = 100

def distance(a, b):
	res = 0
	for i in range(len(a)):
		res += (a[i]-b[i])**2
	return math.sqrt(res)

def cos(a, b):
	ab = 0
	aa = 0
	bb = 0
	for i in range(len(a)):
		ab += a[i] * b[i]
		aa += a[i] ** 2
		bb += b[i] ** 2
	return ab / (math.sqrt(aa)*math.sqrt(bb))

question_filename = "../data/cy_question/data.txt"

if sg == 0:
	context_filename = "data/w2v/context_cbow.txt"
	model = Word2Vec.load("data/w2v/cbow.txt")
else:
	context_filename = "data/w2v/context_sg.txt"
	model = Word2Vec.load("data/w2v/sg.txt")

context = {}
for line in open(context_filename):
	t = line.strip().split(" ")
	cy = t[0]
	vector = []
	for i in range(1, size+1):
		vector.append(float(t[i]))
	context[cy] = vector


total = 0
right = 0
miss = 0

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

	seg_list = ("/ ".join(jieba.cut(q_raw))).encode("utf-8").split("/ ")
	index = seg_list.index("______")
	neighbor = []
	for offset in range(1, window+1):
		if index-offset >= 0:
			neighbor.append(seg_list[index-offset])
		if index+offset < len(seg_list):
			neighbor.append(seg_list[index+offset])
	if len(neighbor) == 0:
		miss += 1
		continue
	vector = [0.0] * size
	cnt = 0
	for w in neighbor:
		if w in model:
			cnt += 1
			for i in range(size):
				vector[i] += model[w][i]
	for i in range(size):
		vector[i] /= cnt
	
	t = []
	if cos == 0:
		if a in context:
			t.append(["A", distance(context[a], vector)])
		if b in context:
			t.append(["B", distance(context[b], vector)])
		if c in context:
			t.append(["C", distance(context[c], vector)])
		if d in context:
			t.append(["D", distance(context[d], vector)])
		t.sort(key=lambda x:x[1], reverse=False)
	else:
		if a in context:
			t.append(["A", cos(context[a], vector)])
		if b in context:
			t.append(["B", cos(context[b], vector)])
		if c in context:
			t.append(["C", cos(context[c], vector)])
		if d in context:
			t.append(["D", cos(context[d], vector)])
		t.sort(key=lambda x:x[1], reverse=True)

	total += 1
	if answer == t[0][0]:
		right += 1

print("system can not answer cnt: %d"%miss)
print("%d/%d\t%.4f"%(right, total, right/float(total)))
