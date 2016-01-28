# encoding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import numpy as np
np.random.seed(11)

from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM

try:
	kind = sys.argv[1]
except:
	print("kind")
	exit()


maxlen = 20
filename_cy = "data/raw/all_statistic.txt"
filename_train = "data/train_%s.txt"%kind
filename_test = "data/test_%s.txt"%kind
filename_model = "data/model/%s2.model"%kind

def loadCy(filename_cy):
	cys = set()
	for line in open(filename_cy):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cys.add(cy)
	cy_indices = dict((c, i) for i, c in enumerate(cys))
	indices_cy = dict((i, c) for i, c in enumerate(cys))
	return cy_indices, indices_cy

def loadWord(filename_train, filename_test):
	words = set()
	for line in open(filename_train):
		for w in line.strip().split("/ "):
			words.add(w)
	for line in open(filename_test):
		for w in line.strip().split("/ "):
			words.add(w)
	word_indices = dict((w, i+1) for i, w in enumerate(words))
	indices_word = dict((i+1, w) for i, w in enumerate(words))
	return word_indices, indices_word

def loadData(filename, cy_indices, word_indices, maxlen):
	sentences = []
	cys = []
	for line in open(filename):
		t = line.strip().split("/ ")
		t = t[-(maxlen+1):]
		while len(t) != maxlen + 1:
			t.insert(0, '')
		sentences.append(t[:-1])
		cys.append(t[-1])

	X = np.zeros((len(sentences), maxlen), dtype=np.int)
	y = np.zeros((len(sentences)), dtype=np.int)
	for i in range(len(sentences)):
		for j in range(len(sentences[i])):
			if sentences[i][j] not in word_indices:
				X[i, j] = 0
			else:
				X[i, j] = word_indices[sentences[i][j]]
		y[i] = cy_indices[cys[i]]
	return X, y

print("Loading data...")
cy_indices, indices_cy = loadCy(filename_cy)
word_indices, indices_word = loadWord(filename_train, filename_test)
X_train, y_train = loadData(filename_train, cy_indices, word_indices, maxlen)
X_test, y_test = loadData(filename_test, cy_indices, word_indices, maxlen)

y_train = np_utils.to_categorical(y_train, len(cy_indices))

print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)

print('Build model...')
model = Sequential()
model.add(Embedding(len(word_indices) + 1, 256, input_length=maxlen))
model.add(LSTM(256))
model.add(Dense(len(cy_indices)))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy", optimizer="sgd", class_mode="categorical")

print("Train...")
model.fit(X_train, y_train, batch_size=32, nb_epoch=1)

print("Save...")
model.save_weights(filename_model, overwrite=True)

#print("Load...")
#model.load_weights(filename_model)

print("Predict...")
y_pred = model.predict(X_test, batch_size=32)

score = 0
for i in range(len(y_pred)):
	arr = []
	for j in range(len(y_pred[i])):
		arr.append([j, y_pred[i][j]])
	arr.sort(key=lambda a:a[1], reverse=True)
	arr = [a[0] for a in arr]
	score += 1.0 / (arr.index(y_test[i])+1)

print("%.4f"%(float(score)/len(y_pred)))


