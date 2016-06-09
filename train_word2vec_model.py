# -*- coding: utf-8 -*-
import gensim
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import os
import logging
import jieba
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
input = open(inp, 'r')
output = open('output.seq', 'w')

if len(sys.argv) < 2:
    print(globals()['__doc__'] % locals())
    sys.exit(1)

# read file and separate words
for line in input.readlines():
    line = line.strip('\n')
    seg_list = jieba.cut(line)
    output.write(' '.join(seg_list) + '\n')

output.close()
output = open('output.seq', 'r')

# initialize the model
# size = the dimensionality of the feature vectors
# window = the maximum distance between the current and predicted word within a sentence
# min_count = ignore all words with total frequency lower than this.
model = Word2Vec(LineSentence(output), size=100, window=3,
                 min_count=5, workers=multiprocessing.cpu_count())

# save model
model.save('output.model')
model.save_word2vec_format('output.vector', binary=False)

# test
model = gensim.models.Word2Vec.load('output.model')
x = model.most_similar([u'奖励'])
for i in x:
    print "Word: {}\t Similarity: {}".format(i[0], i[1])
