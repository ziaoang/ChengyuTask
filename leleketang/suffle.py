# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import random
random.seed(11)



total = open("data_filter_seg_merge/all.txt").read().splitlines()
random.shuffle(total)

df = open("data_filter_seg_merge/all_suffled.txt", 'w')
for t in total:
	df.write(t+'\n')
df.close()