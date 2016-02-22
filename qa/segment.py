# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import jieba

for line in open("data/cy.txt"):
	jieba.add_word(line.strip())

for line in open("data/data.txt"):
	seg_list = jieba.cut(line.strip())
	print("/ ".join(seg_list))






