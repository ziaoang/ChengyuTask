# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re



df = open("meaning.txt", "w")
chengyu_pool = set()
for line in open("data/dictionary.txt"):
	t = line.strip().split('\t')
	id, chengyu, content = t[0].strip(), t[1].strip(), t[2].strip()
	if len(chengyu) != 4*3 or chengyu in chengyu_pool:
		continue
	for item in content.split(r"\n"):
		if "【解释】" in item:
			item_dealed = item.strip()[15:].strip()
			if len(item_dealed) > 0:
				df.write(chengyu + '\t' + item_dealed + '\n')
				chengyu_pool.add(chengyu)
			break
df.close()
