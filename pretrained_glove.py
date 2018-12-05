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


