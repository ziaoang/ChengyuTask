# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import jieba
from collections import defaultdict
from gensim.models import Word2Vec

sg = 1
window = 5
size = 100

sentences = []
for line in open("data/data_seg.txt"):
	sentences.append(line.strip().split("/ "))

model = Word2Vec(sentences, size=size, window=window, min_count=1, workers=4, sg=sg)
if sg == 0:
	model.save("data/w2v/cbow.txt")
else:
	model.save("data/w2v/sg.txt")

cy_set = set()
for line in open("data/cy.txt"):
	cy_set.add(line.strip())

context = defaultdict(list)

for sentence in sentences:
	for i in range(len(sentence)):
		if sentence[i] not in cy_set:
			continue
		neighbor = []
		for j in range(1, window+1):
			if i-j >= 0:
				neighbor.append(sentence[i-j])
			if i+j < len(sentence):
				neighbor.append(sentence[i+j])
		if len(neighbor) == 0:
			continue
		vector = [0.0] * size
		for w in neighbor:
			for j in range(size):
				vector[j] += model[w][j]
		for j in range(size):
			vector[j] /= len(neighbor)
		context[sentence[i]].append(vector)

context_avg = {}
for cy in cy_set:
	context_avg[cy] = [0.0] * size
	if len(context[cy]) == 0:
		continue
	for vector in context[cy]:
		for i in range(size):
			context_avg[cy][i] += vector[i]
	for i in range(size):
		context_avg[cy][i] /= len(context[cy])
	out = "%s"%cy
	for v in context_avg[cy]:
		out += " %f"%v
	print(out)



