# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
from gensim.models import Word2Vec

sentences = []
for line in open("data/data_seg.txt"):
	sentences.append(line.strip().split("/ "))

model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=4, sg=0)
model.save("data/w2v/cbow.txt")
model = Word2Vec(sentences, size=100, window=5, min_count=1, workers=4, sg=1)
model.save("data/w2v/sg.txt")




