# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import jieba
jieba.load_userdict("../data/userdict.txt")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

model = gensim.models.Word2Vec.load("../leleketang/data_filter_seg_merge_split/w2v/all_vector_small_sg.txt")

window_size = 5

total_cnt = 0
right_cnt = 0

cy_set = set()

sf = open("dataset.txt")
while(1):
	line = sf.readline()
	if not line:
		break
	#total_cnt += 1
	q_raw = sf.readline().strip()
	a = sf.readline().strip()
	b = sf.readline().strip()
	c = sf.readline().strip()
	d = sf.readline().strip()
	answer = sf.readline().strip()
	sf.readline()
	sf.readline()

	cy_set.add(a)
	cy_set.add(b)
	cy_set.add(c)
	cy_set.add(d)

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
			if len(context) == 0: # no context can be used
				if answer == "C":
					right_cnt += 0
			else:
				res = []
				if a in model:
					res.append(["A", inner_product(model[a], context)])
				if b in model:
					res.append(["B", inner_product(model[b], context)])
				if c in model:
					res.append(["C", inner_product(model[c], context)])
				if d in model:
					res.append(["D", inner_product(model[d], context)])
				if len(res) != 4:
					if answer == "C":
						right_cnt += 0
				else:
					res.sort(key=lambda x:x[1], reverse=True)
					total_cnt += 1
					if answer == res[0][0]:
						right_cnt += 1
					print(q_raw)
					print("%s\t%.4f"%(a, inner_product(model[a], context)))
					print("%s\t%.4f"%(b, inner_product(model[b], context)))
					print("%s\t%.4f"%(c, inner_product(model[c], context)))
					print("%s\t%.4f"%(d, inner_product(model[d], context)))
					print(answer)
					
			break


print(total_cnt)
print(right_cnt)
print((right_cnt+0.0)/total_cnt)

print("------------")
has_dict = {}
for line in open("../leleketang/statistic/all.txt"):
	t = line.strip().split("\t")
	has_dict[t[0]] = int(t[1])
a = 0
b = 0
for w in cy_set:
	if w in has_dict:
		a += 1
		b += has_dict[w]
print(len(cy_set))
print(a)
print(b/a)
