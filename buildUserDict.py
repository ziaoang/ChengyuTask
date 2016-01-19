# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


df = open("userdict.txt", 'w')
for line in open("meaning.txt"):
	t = line.strip().split('\t')
	df.write(t[0] + '\n')
df.close()