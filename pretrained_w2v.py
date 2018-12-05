from __future__ import print_function. division
from future.utils import iteritems
from builtins import range

# sudo pip install -U future

# pip install gensim
from gensim.models import KeyedVectors

# A few giga bytes
word_vectors = KeyedVectors.load_word2vec_format('../large_files/GoogleNews-vectors-negative300.bin', binary=True)

