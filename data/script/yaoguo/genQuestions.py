# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json

questions = {}

for line in open("raw_leibi.txt"):
	content = line.strip()
	t = json.loads(content)
	for i in range(15):
		qid = t["questions"][i]["id"]
		if qid not in questions:
			questions[qid] = t["questions"][i]

def clean(s):
	return s.strip().replace("\n","").replace("\t","").replace(" ","")

id = 0
for qid in questions:
	id += 1

	q = questions[qid]["question"]
	a = questions[qid]["option_a"]
	b = questions[qid]["option_b"]
	c = questions[qid]["option_c"]
	d = questions[qid]["option_d"]
	answer = questions[qid]["answer"]
	analysis = questions[qid]["analysis"]

	print("-"*10 + " %d "%id + "-"*10)
	print("question: " + clean(q))
	print("A: " + a)
	print("B: " + b)
	print("C: " + c)
	print("D: " + d)
	print("answer: " + clean(answer))
	print("analysis: " + clean(analysis))
	print("\n")



