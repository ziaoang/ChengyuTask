# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

type = "xiaoxue"

df = open("data_filter_seg_merge/%s.txt"%type, 'w')
for filename in os.listdir("data_filter_seg/%s"%type):
	print(filename)
	text = open("data_filter_seg/%s/%s"%(type, filename)).read()
	cy_list, zw_title, zw_content = text.strip().split("\n\n")
	df.write(zw_content+'\n')
df.close()