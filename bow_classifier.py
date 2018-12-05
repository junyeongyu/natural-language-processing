from __future__ import print_function, division
from builtins import range

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from gensim.models import KeyedVectors

train = pd.read_csv('../filename.txt', header=None, sep='\t')
test = pd.read_csv('../filename.txt', header=None, sep='\t')
train.columns = ['label', 'content']
test.columns = ['label', 'content']

class GloveVectorizer:
  def __init__(self):
    print('Loading word vectors...')
    word2vec = {}
    embedding = []
    idx2word = []
    with open('../large_files/glove.6B/glove.6B.50d.txt') as f:
      for line in f:
        values = line.split()
        word = values[0]
        vec = np.asarray(values[1:], dtype='float32')
        word2vec[word] = vec
        embedding.append(vec)
        idx2word.append(word)
      print('Found %s word vectors.' % len(word2vec))
      
      # save for later
      self.word2vec = word2vec
      self.embedding = np.array(embedding)
      self.word2idx = {v:k for k,v in enumerate(idx2word)}
      self.V, self.D = self.embedding.shape
    
    def fit(self, data):
      pass
    
    def transform(self, data):
      X = np.zeros((len(data), self.D))
      
    def fit_transform(self, data):
      self.fit(data)
      return self.transform(data)
