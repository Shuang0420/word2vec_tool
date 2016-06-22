# word2vec_example

## 使用方法
### 用python jieba进行分词，训练 word2vec 模型
<pre>python train_word2vec_model.py all.txt</pre>

### 已经分好词的文件训练 word2vec 模型
<pre>python segprocessed_train_word2vec_model.py filename</pre>

### 用同一目录下的 qqseg_new 工具分词
<pre>python word2vec.py -input inputfile -output outputfile
usage: word2vec.py [-h] [-input INP] [-output OUTPUT] [-window WINDOW]
                   [-size SIZE] [-min_count MIN_COUNT] [-cbow_mean CBOW_MEAN]
                   [-sg SG] [-iters ITERS]

optional arguments:
  -h, --help            show this help message and exit
  -input INP            original input file name
  -output OUTPUT        output model name
  -window WINDOW        the maximum distance between the current and predicted
                        word within a sentence
  -size SIZE            the dimensionality of the feature vectors
  -min_count MIN_COUNT  ignore all words with total frequency lower than this
  -cbow_mean CBOW_MEAN  if 0, use the sum of the context word vectors. If 1
                        (default), use the mean. Only applies when cbow is
                        used.
  -sg SG                sg defines the training algorithm. By default (sg=0),
                        CBOW is used. Otherwise (sg=1), skip-gram is employed.
  -iters ITERS          number of iterations (epochs) over the corpus.</pre>


### 计算词向量的模并从大到小排序，输出word - norm of vector
<pre>python normVector.py
</pre>
