# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
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


def initialize():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', action='store', dest='inp', default='',
                        help='original input file name')
    parser.add_argument('-output', action='store', dest='output', default='',
                        help='output model name')
    parser.add_argument('-window', action='store', dest='window', default='5',
                        help='the maximum distance between the current and predicted word within a sentence')
    parser.add_argument('-size', action='store', dest='size',
                        default='100', help='the dimensionality of the feature vectors')
    parser.add_argument('-min_count', action='store', dest='min_count', default='5',
                        help='ignore all words with total frequency lower than this')
    parser.add_argument('-cbow_mean', action='store', dest='cbow_mean', default='1',
                        help='if 0, use the sum of the context word vectors. If 1 (default), use the mean. Only applies when cbow is used.')
    parser.add_argument('-sg', action='store', dest='sg', default='0',
                        help='sg defines the training algorithm. By default (sg=0), CBOW is used. Otherwise (sg=1), skip-gram is employed.')
    parser.add_argument('-iters', action='store', dest='iters', default='5',
                        help='number of iterations (epochs) over the corpus.')
    parser.add_argument('-model', action='store', dest='model_name',
                        help='if you want to retrain the model, just give the model.')
    return parser.parse_args()


def processFile(inp):
    path = os.getcwd()
    # preprocess
    # UTF-8 --> GBK
    os.system('iconv -c -t gbk ' + inp + '>' + inp + '.gbk')
    # split words
    os.chdir(os.getcwd() + '/' + 'qqseg_new')
    if '/' in inp:
        os.system('./SegTester --input_file=' +
                  inp + '.gbk' + ' --output_file=../output.seg --log_dir=log')
    else:
        os.system('./SegTester --input_file=../' +
                  inp + ' --output_file=../output.seg --log_dir=log')
    os.chdir(path)
    # GBK --> UTF-8
    os.system('enca -L zh_CN -x UTF-8 output.seg')
    os.system('enca -L zh_CN -x UTF-8 ' + inp)
    os.system('rm -rf ' + inp + '.gbk')


def trainModel(args):
    # initialize parameters and process file
    window = int(args.window)
    size = int(args.size)
    min_count = int(args.min_count)
    cbow_mean = int(args.cbow_mean)
    sg = int(args.sg)
    iters = int(args.iters)
    model_name = args.model_name
    inp = args.inp
    output = args.output
    if not (inp and output):
        print 'Please identify the input and output. Use the command "python word2vec.py -input filename -output filename"'
        exit(1)
    processFile(inp)
    if not model_name:
        # train model
        model = Word2Vec(LineSentence('output.seg'), size=size, window=window,
                         min_count=min_count, sg=sg, iter=iters, cbow_mean=cbow_mean, workers=multiprocessing.cpu_count())
        # save model
        model.save(output)
        model.save_word2vec_format(output + '.vector', binary=False)
    else:
        f = open('output.seg', 'r')
        sentences = f.readlines()
        total_examples = len(sentences)
        total_word = 0
        total_words = [total_word + len(s.split()) for s in sentences]
        total_words = sum(total_words)
        sentences = [s.decode('utf8') for s in sentences]
        model = Word2Vec.load(model_name)
        model.train(sentences, total_examples=total_examples,
                    total_words=total_words)
        model.save(output)


if __name__ == '__main__':
    args = initialize()
    trainModel(args)
