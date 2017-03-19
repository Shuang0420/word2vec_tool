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

def simWords(modelname):
    global resultsList
    wordsList=generateWords(modelname)
    resultsList=dict()
    for word in wordsList:
        results = model.most_similar(word.decode('utf8'))
        resultsList[word]=results[0]
    l = sorted(resultsList.items(), key=lambda cosList: -cosList[1][1])
    flag = True
    sumValue=0
    for i in range(0,len(l)):
        sumValue += l[i][1][1]
        if flag:
            print '{}\t{}\t{}'.format(l[i][0], l[i][1][0],l[i][1][1])
            flag=False
        else:
            flag=True
    avgValue = sumValue / len(l)
    print avgValue
        #for i in results:
        #    print '{}\t{}'.format(i[0], i[1])
    #simWordsSingle()



def simWordsSingle():
    while (1):
        w = raw_input('enter the word ')
        word = []
        for i in w.split():
            i = i.decode('utf8')
            word.append(i)
        results = model.most_similar(word)
        for i in results:
            print '{}\t{}'.format(i[0], i[1])

def generateWords(modelname):
    wordsList=[]
    filename = modelname + '.vector'
    f = open(filename,'r')
    for line in f:
        word=line.split(' ',1)[0]
        if len(word)>=6:
            wordsList.append(word)
    return wordsList

if __name__ == '__main__':
    # load model
    #modelname = raw_input('enter the model you want to check ')
    modelname = sys.argv[1]
    model = Word2Vec.load(modelname)
    simWords(modelname)
