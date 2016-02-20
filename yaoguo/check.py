

import sys
import json


a = []

for line in open("data.txt"):
	content = line.strip()
	t = json.loads(content)
	for i in range(15):
		qid = t["questions"][i]["id"]
		a.append(qid)

print('-'*20)
print(len(a))
print(len(set(a)))

