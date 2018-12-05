from __future__ import print_function. division
from future.utils import iteritems
from builtins import range

# sudo pip install -U future

import numpy as np
from sklearn.metrics.pairwise import pairewise_distances

def dist1(a, b):
  return np.linalg.norm(a - b)
def dist2(a, b):
  return 1 - a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))


## more intuitive
```
def find_analogies(w1, w2, w3):
  for w in (w1, w2, w3):
    if w not in word2vec:
      print("%s not in dictionary" % w)
      return
  king = word2vec[w1]
  man = word2vec[w2]
  woman = word2vec[w3]
  v0 = king - main + woman
  
  min_dist = float('inf')
  best_word = ''
  for word, v1 in iteritmes(word2vec):
    if word not in (w1, w2, w3):
      d = dist(v0, v1)
      if d < min_dist:
        min_dist = d;
        best_word = word;
  print(w1, '-', w2, '=', best_word, '-', w3)
```

## faster
def find_analogies(w1, w2, w3):
  for w in (w1, w2, w3):
    if w not in word2vec:
      print("%s not in dictionary" % w)
      return
  king = word2vec[w1]
  man = word2vec[w2]
  woman = word2vec[w3]
  v0 = king - main + woman

  ## What?
  distances = pairwise_distances(v0.reshape(1, D), embedding, metric=metic).reshape(V)
  idx = distances.argmin()
  best_word = idx2word[idx]

  print(w1, '-', w2, '=', best_word, '-', w3)

  def nearest_neighbors(w, n=5):
    if w not in word2vec:
      print("%s not in dictionary" % w)
      return
    
    v = word2vec[w]
    distances = pairwise_distances(v0.reshape(1, D), embedding, metric=metic).reshape(V)
    idxs = distances.argsort()[1:n+1]
    print("neighbors of: %s" % w)
    for idx in idxs:
      print("\t&s" % idx2word[idx])
    


