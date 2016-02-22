# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import math
import jieba
from collections import defaultdict
from gensim.models import Word2Vec

window = 5
size = 100

def distance(a, b):
	res = 0
	for i in range(len(a)):
		res += (a[i]-b[i])**2
	return res

def cos(a, b):
	ab = 0
	aa = 0
	bb = 0
	for i in range(len(a)):
		ab += a[i] * b[i]
		aa += a[i] * a[i]
		bb += b[i] * b[i]
	return ab / (math.sqrt(aa)*math.sqrt(bb))

context = {}
#for line in open("data/context_cbow.txt"):
for line in open("data/context_sg.txt"):
	t = line.strip().split(" ")
	cy = t[0]
	vector = []
	for i in range(1, size+1):
		vector.append(float(t[i]))
	context[cy] = vector

#model = Word2Vec.load("data/w2v/cbow.txt")
model = Word2Vec.load("data/w2v/sg.txt")

total = 0
right = 0

sf = open("../data/cy_question/data.txt")
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
	
	for i in range(len(seg_list)):
		if seg_list[i] == "______":
			neighbor = []
			for j in range(1, window+1):
				if i-j >= 0:
					neighbor.append(seg_list[i-j])
				if i+j < len(seg_list):
					neighbor.append(seg_list[i+j])
			if len(neighbor) == 0:
				continue
			vector = [0.0] * size
			for w in neighbor:
				if w in model:
					for j in range(size):
						vector[j] += model[w][j]
			for j in range(size):
				vector[j] /= len(neighbor)
			t = []
			if a in context:
				t.append(["A", distance(context[a], vector)])
			if b in context:
				t.append(["B", distance(context[b], vector)])
			if c in context:
				t.append(["C", distance(context[c], vector)])
			if d in context:
				t.append(["D", distance(context[d], vector)])
			t.sort(key=lambda x:x[1], reverse=False)
			total += 1
			if answer == t[0][0]:
				right += 1

print(total)
print(right)
