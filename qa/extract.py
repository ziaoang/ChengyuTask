# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os


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


def exist(content):
	for cy in cy_set:
		if cy in content:
			return True
	return False

print("chengyu cnt: %d"%len(cy_set))


path_list = []
for t in os.walk("../data/news/THUCNews"):
	for f in t[2]:
		filepath = "%s/%s"%(t[0], f)
		path_list.append(filepath)
for t in os.walk("../data/zuowen/LeLeKeTangZuoWen"):
	for f in t[2]:
		filepath = "%s/%s"%(t[0], f)
		path_list.append(filepath)
print("file cnt: %d"%len(path_list))

df = open("data/data.txt", "w")
for filepath in path_list:
	print(filepath)
	for line in open(filepath):
		if exist(line):
			df.write(line.strip()+"\n")
df.close()
