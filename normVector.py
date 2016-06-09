# calculate the norm of word vectors and sort

import numpy as np
f = open('output.vector', 'r')
vecDict = dict()
flag = True
for line in f:
    # ignore the first line
    if (flag):
        flag = False
        continue
    line = line.strip('\n')
    word = line.split(' ', 1)[0]
    v = line.split(' ', 1)[1]
    try:
        vector = [float(i) for i in v.split()]
        x = np.array(vector)
        Lx = np.sqrt(x.dot(x))
        vecDict[word] = Lx
    except ValueError, e:
        print e

sortedVecDict = sorted(vecDict.items(), key=lambda vecDict: -vecDict[1])
for i in sortedVecDict:
    print "{}\t {}".format(i[0], i[1])
