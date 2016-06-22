# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os
import logging
import re
import multiprocessing
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# logging information
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

# get input file, text format
inp = sys.argv[1]


# initialize the model
# size = the dimensionality of the feature vectors
# window = the maximum distance between the current and predicted word within a sentence
# min_count = ignore all words with total frequency lower than this.
model = Word2Vec(LineSentence(inp), size=100, window=3,
                 min_count=5, workers=multiprocessing.cpu_count())

# save model
model.save('output.model')
model.save_word2vec_format('output.vector', binary=False)
