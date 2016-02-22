# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import random
from collections import defaultdict

cy_dict = defaultdict(int)

sf = open("data.txt")
while(1):
	line = sf.readline()
	if not line:
		break
	q_raw = sf.readline().strip()
	a = sf.readline().strip()
	b = sf.readline().strip()
	c = sf.readline().strip()
	d = sf.readline().strip()
	answer = sf.readline().strip()
	sf.readline()
	sf.readline()
	
	cy_dict[a] += 1
	cy_dict[b] += 1
	cy_dict[c] += 1
	cy_dict[d] += 1


t = []
for cy in cy_dict:
	t.append([cy, cy_dict[cy]])
t.sort(key=lambda x:x[1], reverse=True)

for x in t:
	print("%s\t%d"%(x[0],x[1]))
