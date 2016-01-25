# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

type = "gaozhong"

word_pool = set()
fname = "data_filter_seg_split/vector_gaozhong.txt"
sentences = []
for line in open("data_filter_seg_split/gaozhong_train.txt"):
	for s in line.strip().split('\t')[1:]:
		sentences.append(s.strip().split("/ "))
		for word in s.strip().split("/ "):
			word_pool.add(word)
model = gensim.models.Word2Vec(sentences, min_count=1, size=200, window = 5)
model.save(fname)


all = 0
right = 0
model = gensim.models.Word2Vec.load(fname)
for line in open("data_filter_seg_split/gaozhong_test.txt"):
	t = line.strip().split('\t')
	cy = t[0]
	for sentence in t[1:]:
		all += 1
		words = sentence.strip().split("/ ")
		cy_index = words.index(cy)
		neighbor = []
		for i in [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]:
			if cy_index+i >= 0 and cy_index+i < len(words):
				if words[i] in word_pool:
					neighbor.append(words[i])
		if len(neighbor) != 0:
			t = model.most_similar(positive=neighbor, negative=[], topn=10)
			if cy in [a[0] for a in t]:
				right += 1
			#if t[0][0] == cy:
			#	right += 1

print(all)
print(right)




