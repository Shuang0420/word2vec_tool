# word2vec_example

## 使用方法
### 用python jieba进行分词，训练 word2vec 模型
<pre>python train_word2vec_model.py all.txt</pre>


### 训练 word2vec 模型
<pre>python word2vec.py -input inputfile -output outputfile</pre>
<pre>
usage: word2vec.py [-h] [-input INPUT] [-output OUTPUT] [-window WINDOW]
                   [-size SIZE] [-min_count MIN_COUNT] [-cbow_mean CBOW_MEAN]
                   [-sg SG] [-iters ITERS] [-model MODEL_NAME]
                   [-qqseg SEG_REQUIRED]

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
  -iters ITERS          number of iterations (epochs) over the corpus.
  -model MODEL_NAME     if you want to retrain the model, just give the model.
  -qqseg SEG_REQUIRED   if 0(default), assume the text is already segmented.
                        If 1, run segmentation tool first.
</pre>

### 计算词向量的模并从大到小排序，输出word - norm of vector
<pre>python normVector.py
</pre>


### 测试效果
<pre>python word2vec_testTool.py
enter the model you want to check guomei.model
2016-06-27 16:51:36,856: INFO: loading Word2Vec object from guomei.model
2016-06-27 16:51:36,973: INFO: setting ignored attribute syn0norm to None
2016-06-27 16:51:36,973: INFO: setting ignored attribute cum_table to None
2016-06-27 16:51:46,343: INFO: precomputing L2-norms of word weight vectors
enter the word 烹饪
烹调	0.62442278862
中餐	0.534122824669
解冻	0.48883074522
加热	0.479849278927
食用	0.470198184252
菜肴	0.466752141714
做饭	0.462529540062
炖肉	0.457395881414
熬汤	0.446689903736
慢火	0.427767693996
enter the word 订单
定单	0.778802156448
运单	0.682202041149
账号	0.611731410027
账户	0.587948918343
帐号	0.585913598537
下单	0.5846991539
单号	0.58408164978
imei	0.583274126053
退款	0.578039348125
货物	0.576778292656</pre>
