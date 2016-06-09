# word2vec_example

#使用方法
### 用python jieba进行分词，训练 word2vec 模型
python train_word2vec_model.py all.txt

### 已经分好词的文件训练 word2vec 模型
python segprocessed_train_word2vec_model.py all.seg

### 计算词向量的模并从大到小排序，输出word - norm of vector
python normVector.py
