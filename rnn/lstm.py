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



def loadCy(filename_cy):
	cys = set()
	for line in open(filename):
		t = line.strip().split('\t')
		cy, cnt = t[0], int(t[1])
		if cnt >= 1000:
			cys.add(cy)
	cy_indices = dict((c, i+1) for i, c in enumerate(cys))
	indices_cy = dict((i+1, c) for i, c in enumerate(cys))
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

def loadData(filename, cy_indices, word_indices, maxlen=20):
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


filename_cy = "data/all_statistic.txt"
filename_train = "data/pre_train.txt"
filename_test = "data/pre_test.txt"

print("Loading data...")
cy_indices, indices_cy = loadCy(filename_cy)
word_indices, indices_word = loadWord(filename_train, filename_test)
X_train, y_train = loadData(filename_train, cy_indices, word_indices)
X_train, y_train = loadData(filename_train, cy_indices, word_indices)

print('Build model...')
model = Sequential()
model.add(Embedding(len(word_indices) + 1, 128, input_length=maxlen))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', class_mode="categorical")

print("Train...")
model.fit(X_train, y_train, batch_size=32, nb_epoch=1, show_accuracy=True)

print("Save...")
save_weights("data/1.model", overwrite=True)

print("Predict...")
y_pred = model.predict_proba(X_test, batch_size=32)

scroe = 0
for i in range(len(y_pred)):
	arr = []
	for j in range(len(y_pred[i])):
		arr.append([j, y_pred[i][j]])
	arr.sort(key=lambda a:a[1], reverse=True)
	arr = [a[0] for a in arr]
	score += 1.0 / arr.index(y_test[i])

print("%.4f"%score)