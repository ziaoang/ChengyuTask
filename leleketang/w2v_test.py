# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


size = "big"
#size = "small"
method = "sg"
#method = "cbow"


model_filename = "data_filter_seg_merge_split/w2v/all_vector_%s_%s.txt"%(size, method)
res_filename = "data_filter_seg_merge_split/res/res_%s_%s.txt"%(size, method)
test_filename = "data_filter_seg_merge_split/all_test.txt"

model = gensim.models.Word2Vec.load(model_filename)

def load():
	POOL = {}
	for line in open("statistic/all.txt"):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			POOL[cy] = cnt
	return POOL

POOL = load()

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

def rank(neighbor):
	context = []
	for w in neighbor:
		if len(context) == 0:
			for i in range(len(model[w])):
				context.append(model[w][i])
		else:
			for i in range(len(model[w])):
				context[i] += model[w][i]
	res = []
	for cy in POOL:
		res.append([cy, inner_product(model[cy], context)])
	res.sort(key=lambda a:a[1], reverse=True)
	res = [t[0] for t in res]
	return res

total = 0
right = 0
lineNo = 0
for line in open(test_filename):
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
		top = rank(neighbor)
		right += 1.0 / (top.index(cy)+1)

df = open(res_filename, 'w')
df.write("%.4f\t%d\t%.4f\n"%(right, total, right/float(total)))
df.close()
