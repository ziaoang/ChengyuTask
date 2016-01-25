# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os


df = open("data_filter_seg_merge/all.txt", "w")
for type in ["xiaoxue", "chuzhong", "gaozhong"]:
	for line in open("data_filter_seg_merge/%s.txt"%type):
		df.write(line.strip()+'\n')
df.close()
