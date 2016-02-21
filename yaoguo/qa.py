# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import jieba
jieba.load_userdict("../data/userdict.txt")

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

model = load_model("../leleketang/data_filter_seg_merge_split/w2v/all_vector_small_sg.txt")

window_size = 5

sf = open("dataset.txt")
while(1):
	sf.readline()
	q_raw = sf.readline().strip()
	a = sf.readline().strip()
	b = sf.readline().strip()
	c = sf.readline().strip()
	d = sf.readline().strip()
	answer = sf.readline().strip()
	sf.readline()
	sf.readline()

	if a not in model:
		print(a)
	if b not in model:
		print(b)
	if c not in model:
		print(c)
	if d not in model:
		print(d)

	seg_list = jieba.cut(q_raw)
	q_split = ("/ ".join(seg_list)).encode("utf-8")
	q_seg = q_split.split("/ ")

	for i in range(len(q_seg)):
		if q_seg[i] == '______':
			context = []
			for j in range(-window_size, window_size+1):
				if j == 0 or i+j < 0 or i+j >= len(q_seg):
					continue
				w = q_seg[i+j]
				if w not in model:
					continue
				if len(context) == 0:
					for k in range(len(model[w])):
						context.append(model[w][k])
				else:
					for k in range(len(model[w])):
						context[i] += model[w][k]
			break




