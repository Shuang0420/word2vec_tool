# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec
import os
import logging
import re
import multiprocessing
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# logging information
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

def simWords():
    while (1):
        w = raw_input('enter the word ')
        word = []
        for i in w.split():
            i = i.decode('utf8')
            word.append(i)
        results = model.most_similar(word)
        for i in results:
            print '{}\t{}'.format(i[0], i[1])


if __name__ == '__main__':
    # load model
    modelname = raw_input('enter the model you want to check ')
    model = Word2Vec.load(modelname)
    simWords()
