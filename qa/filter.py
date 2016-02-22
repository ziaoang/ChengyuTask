# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

cy_set = set()
sf = open("../data/cy_question/data.txt")
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

	cy_set.add(a)
	cy_set.add(b)
	cy_set.add(c)
	cy_set.add(d)

for cy in cy_set:
	print(cy)



				
			




