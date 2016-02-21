# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import jieba
jieba.load_userdict("../data/userdict.txt")

lineNo = 0
for line in open("dataset.txt"):
	lineNo += 1
	if (lineNo+7) % 9 == 0:
		question = line.strip().replace(' ', '')
		question_seg = jieba.cut(question)
		if "______" not in question_seg:
			print("error")
		# print("/ ".join(question_seg))




