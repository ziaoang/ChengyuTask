# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import jieba
jieba.load_userdict("userdict.txt")

df = open("meaning_seg.txt", 'w')
for line in open("meaning.txt"):
	t = line.strip().split('\t')
	seg_list = jieba.cut(t[1].replace(' ', ''))
	df.write("%s\t%s\n"%(t[0], '/ '.join(seg_list)))
df.close()


