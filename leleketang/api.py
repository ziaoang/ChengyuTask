# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


try:
	size = sys.argv[1] # big or small
	method = sys.argv[2] # sg or cbow
except:
	print("size method")
	exit()

window_size = 5
statistic_filename = "statistic/all.txt"
test_filename = "data_filter_seg_merge_split/all_test.txt"
model_filename = "data_filter_seg_merge_split/w2v/all_vector_%s_%s.txt"%(size, method)
res_filename = "data_filter_seg_merge_split/res/res_%s_%s.txt"%(size, method)

def load_model(filename):
	return gensim.models.Word2Vec.load(filename)

def load_cy_dict(filename):
	cy_dict = {}
	for line in open(filename):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cy_dict[cy] = cnt
	return cy_dict

def loadContext(paragraph, cy_dict, window_size):
	contexts = []
	t = paragraph.strip().split("/ ")
	for i in range(len(t)):
		if t[i] in cy_dict: # t[i] is a cy
			context = [[], [], []] # left, middle, right
			for j in range(-window_size, 0):
				if i+j >= 0:
					context[0].append(t[i+j])
			context[1].append(t[i])
			for j in range(1, window_size+1):
				if i+j < len(t):
					context[2].append(t[i+j])
			contexts.append(context)
	return contexts

def inner_product(a, b):
	res = 0
	for i in range(len(a)):
		res += a[i] * b[i]
	return res

def rank(neighbor, model, cy_dict):
	context = []
	for w in neighbor:
		if w not in model:
			continue
		if len(context) == 0:
			for i in range(len(model[w])):
				context.append(model[w][i])
		else:
			for i in range(len(model[w])):
				context[i] += model[w][i]
	res = []
	if len(context) == 0: # no context can be used
		for cy in cy_dict:
			res.append([cy, cy_dict[cy]])
	else:
		for cy in cy_dict:
			res.append([cy, inner_product(model[cy], context)])
	res.sort(key=lambda a:a[1], reverse=True)
	return res

def loadParagraph(filename):
	paragraphs = []
	for line in open(filename):
		paragraphs.append(line.strip())
	return paragraphs

cy_dict = load_cy_dict()
model = load_model()

total = 0
score = 0.0
p1 = 0
paragraphs = loadParagraph(test_filename)
for paragraph in paragraphs:
	contexts = loadContext(paragraph, cy_dict, window_size)
	for context in contexts:
		total += 1
		neighbor = context[0] + context[2]
		cy = context[1][0]
		result = rank(neighbor, model, cy_dict)
		result_cy = [t[0] for t in result]
		score += 1.0 / (result_cy.index(cy)+1)
		if result_cy[0] == cy:
			p1 += 1

df = open(res_filename, 'w')
df.write("nb_total: %d\n"%total)
df.write("score: %.4f\n"%score)
df.write("nb_p1: %d\n"%p1)
df.write("MRR: %.4f\n"%(score/float(total)))
df.write("Precision: %.4f\n"%(p1/float(total)))
df.close()
