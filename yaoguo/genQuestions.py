# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json

questions = {}

for line in open("raw.txt"):
	content = line.strip()
	t = json.loads(content)
	for i in range(15):
		qid = t["questions"][i]["id"]
		if qid not in questions:
			questions[qid] = t["questions"][i]

for qid in questions:
	a = questions[qid]["option_a"]
	b = questions[qid]["option_b"]
	c = questions[qid]["option_c"]
	d = questions[qid]["option_d"]
	if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
		print("-"*20)
		print(questions[qid]["question"])
		print(questions[qid]["option_a"])
		print(questions[qid]["option_b"])
		print(questions[qid]["option_c"])
		print(questions[qid]["option_d"])
		print(questions[qid]["answer"])
		print("\n")
