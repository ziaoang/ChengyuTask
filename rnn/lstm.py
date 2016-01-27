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

maxlen = 20
batch_size = 32


# cy-index hash
cys = set()
for line in open("data/all_statistic.txt"):
	t = line.strip().split('\t')
	cy, cnt = t[0], int(t[1])
	if cnt >= 1000:
		cys.add(cy)
cy_indices = dict((c, i+1) for i, c in enumerate(cys))
indices_cy = dict((i+1, c) for i, c in enumerate(cys))


# word-index hash
words = set()
for line in open("data/pre.txt"):
	t = line.strip().split("/ ")
	for w in t:
		words.add(w)
print('total words:', len(words))
word_indices = dict((w, i+1) for i, w in enumerate(words))
indices_word = dict((i+1, w) for i, w in enumerate(words))

max_features = len(word_indices) + 1

# cut the input paragraph
sentences = []
next_words = []
for line in open("data/pre.txt"):
	t = line.strip().split("/ ")
	t = t[-(maxlen+1):]
	while len(t) != maxlen + 1:
		t.insert(0, '')
	sentences.append(t[:-1])
	next_words.append(t[-1])
print('nb sequences:', len(sentences))


# vectorization
print('Vectorization...')
X = np.zeros((len(sentences), maxlen), dtype=np.int)
y = np.zeros((len(sentences)), dtype=np.int)
for i in range(len(sentences)):
	for j in range(len(sentences[i])):
		if sentences[i][j] == '':
			X[i, j] = 0
		else:
			X[i, j] = word_indices[sentences[i][j]]
	y[i] = cy_indices[next_words[i]]


# build model
print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 128, input_length=maxlen))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', class_mode="binary")

print("Train...")
model.fit(X, y, batch_size=batch_size, nb_epoch=3, show_accuracy=True)

