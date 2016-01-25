# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


fname = "data_filter_seg_merge_split/all_vector.txt"
sentences = []
lineNo = 0
for line in open("data_filter_seg_merge_split/all_train.txt"):
	lineNo += 1
	if lineNo % 10000 == 0:
		print(lineNo)
	sentences.append(line.strip().split("/ "))
model = gensim.models.Word2Vec(sentences, min_count=1, size=200, window = 5)
model.save(fname)

