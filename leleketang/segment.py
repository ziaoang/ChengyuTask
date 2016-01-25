# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import jieba
jieba.load_userdict("../userdict.txt")


for filename in os.listdir("data_filter/xiaoxue"):
	print(filename)
	text = open("data_filter/xiaoxue/"+filename).read()
	cy_list, zw_title, zw_content = text.strip().split("\n\n")
	zw_content_seg = ""
	for t in zw_content.strip().split('\n'):
		seg_list = jieba.cut(t.replace(' ', ''))
		zw_content_seg += '/ '.join(seg_list) + '\n'
	df = open("data_filter_seg/xiaoxue/"+filename, 'w')
	df.write("%s\n\n%s\n\n%s"%(cy_list, zw_title, zw_content_seg))
	df.close()


