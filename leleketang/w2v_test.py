# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



fname = "data_filter_seg_merge_split/all_vector.txt"
model = gensim.models.Word2Vec.load(fname)

POOL = {}
for line in open("statistic/all.txt"):
	t = line.strip().split('\t')
	cy, cnt = t[0], int(t[1])
	if cnt >= 1000:
		POOL[cy] = cnt

total = 0
right = 0
lineNo = 0
for line in open("data_filter_seg_merge_split/all_test.txt"):
	lineNo += 1
	if lineNo % 10000 == 0:
		print(lineNo)
	t = line.strip().split("/ ")
	for cy in POOL:
		if cy not in t:
			continue
		cy_index = t.index(cy)
		neighbor = []
		for i in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
			if cy_index+i >= 0 and cy_index+i < len(t):
				if t[cy_index+i] in model:
					neighbor.append(t[cy_index+i])
		if len(neighbor) == 0:
			continue
		total += 1
		top = model.most_similar(positive=neighbor, negative=[], topn=10)
		if cy in [a[0] for a in top]:
			# print(line.strip())
			right += 1

print(total)
print(right)




