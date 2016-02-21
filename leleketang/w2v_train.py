# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


for type in ["big", "small"]:
	# skip-gram
	fname = "data_filter_seg_merge_split/w2v/all_vector_%s_sg_10.txt"%type
	sentences = []
	lineNo = 0
	for line in open("data_filter_seg_merge_split/all_train_%s.txt"%type):
		lineNo += 1
		if lineNo % 10000 == 0:
			print(lineNo)
		sentences.append(line.strip().split("/ "))
	model = gensim.models.Word2Vec(sentences, min_count=1, size=200, window = 10, sg = 1)
	model.save(fname)
	# cbow
	fname = "data_filter_seg_merge_split/w2v/all_vector_%s_cbow_10.txt"%type
	sentences = []
	lineNo = 0
	for line in open("data_filter_seg_merge_split/all_train_%s.txt"%type):
		lineNo += 1
		if lineNo % 10000 == 0:
			print(lineNo)
		sentences.append(line.strip().split("/ "))
	model = gensim.models.Word2Vec(sentences, min_count=1, size=200, window = 10, sg = 0)
	model.save(fname)

