# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os


cy_set = set()
for line in open("data/cy.txt"):
	cy_set.add(line.strip())

def exist(content):
	for cy in cy_set:
		if cy in content:
			return True
	return False

path_list = []
for t in os.walk("../data/news/THUCNews"):
	for f in t[2]:
		filepath = "%s/%s"%(t[0], f)
		path_list.append(filepath)
for t in os.walk("../data/zuowen/LeLeKeTangZuoWen"):
	for f in t[2]:
		filepath = "%s/%s"%(t[0], f)
		path_list.append(filepath)

for filepath in path_list:
	for line in open(filepath):
		if exist(line):
			print(line.strip())

