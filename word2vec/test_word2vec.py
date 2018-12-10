#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import gensim, logging
from gensim.models.word2vec import LineSentence
from gensim.test.utils import common_texts, get_tmpfile, datapath
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# 模型的训练
def train():
    # 1. 加载语句
    sentences = LineSentence(datapath('lee_background.cor'))
    # 2. 建立词向量模型
    # 2.1 建立一个空的词向量模型
    model = Word2Vec()
    for sentence in sentences:
        print(sentence)
    # print(sentences)

        # 2.2 遍历语料库建立神经网络模型
        model.build_vocab(sentence)
    # # 2.3 训练模型
    # model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
    # # 3. 保存
    # # 3.1 前一组方法保存的文件不能利用文本编辑器查看但是保存了训练的全部信息，可以在读取后追加训练
    # model.save('./output_data/MyModel')
    # # 3.2 后一组方法保存为word2vec文本格式但是保存时丢失了词汇树等部分信息，不能追加训练
    # # model.save_word2vec_format('/tmp/mymodel.txt', binary=False)
    # # model.save_word2vec_format('/tmp/mymodel.bin.gz', binary=True)
    # print(model['computer'])
    # print(type(model['computer']))
    # # model.most_similar('男人')

def test():
    path = get_tmpfile("word2vec.model")
    path2 = get_tmpfile("wordvectors.kv")
    model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
    model.save("word2vec.model")
    model.wv.save(path2)
    vector = model.wv['computer']

    sentences = LineSentence(datapath('lee_background.cor'))
    for sentence in sentences:
        print(sentence)

    # print(vector)
    # wv = KeyedVectors.load("model.wv", mmap='r')
    # vector = wv['computer']

    # 继续训练这个模型
    model = Word2Vec.load("word2vec.model")
    model.train([["hello", "world"]], total_examples=1, epochs=1)

    vector = model.wv['computer']

    # 模型已经训练好了，可以直接使用
    word_vectors = model.wv
    # del model
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # # 准备输入
    # sentences = [['first', 'sentence'], ['second', 'sentence']]
    # model = gensim.models.word2vec(sentences, min_count=1)
if __name__ == '__main__':
    train()
