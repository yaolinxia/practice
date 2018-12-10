#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import jieba
import os
from gensim.models import word2vec
import logging

# 1. 对于给定的语料库，首先要进行分词
def segment_file(read_path, write_path):
    f2 = open(write_path, 'a', encoding='utf-8')
    # 1.1 判断路径是否存在
    if os.path.exists(read_path):
        with open(read_path, 'r', encoding='utf-8') as f:
            # f.readlines() 读取全部内容
            text = f.readlines()
            for line in text:
                line.replace('\t', '').replace('\n', '').replace(' ', '')
                seg_text = jieba.cut(line, cut_all=False)
                # print(" ".join(seg_text))
                # with open(write_path, 'a', encoding='utf-8') as f2:
                f2.write(" ".join(seg_text), )
                # print(" ".join(seg_text))
            f2.close()

# 2. 使用Word2vec模型
def train(file_path):
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    # 加载语料
    sentences = word2vec.Text8Corpus(file_path)
    # 训练skip-gram模型， 默认windows=5
    model = word2vec.Word2Vec(sentences, size=200)
    # print(model)
    # try:
    #     y1 = model.similarity(u"国家", u"国务院")
    # except KeyError:
    #     y1 = 0
    # print("国家，国务院的相似度为：", y1)
    return model

# 3. 计算两个词之间的相似度
def calc_similarity(my_model):
    try:
        y1 = my_model.similarity(u"交通", u"交通事故")
    except KeyError:
        y1 = 0
    print("交通，交通事故的相似度为：", y1)

# 4. 寻找对于关系
def find_Correspondence(my_model):
    print("交通事故，赔偿-")
    y = my_model.most_similar([u'交通事故', u'赔偿'], [u'书'], topn=3)
    for item in y:
        print(item[0], item[1])

# 5. 计算两个词的相关词列表
def find_twowords(my_model):
    y = my_model.most_similar(u"交通", topn=20)
    print("和交通相关的词有：")
    for item in y:
        print(item[0], item[1])

# 6. 寻找不合群的词
def find_different(my_model):
    y = my_model.doesnt_match(u"交通 肇事 罪名 很".split())
    print("不合群的词：", y)


# 7. 保存模型，便于以后重用
def save_model(my_model):
    my_model.save("my_model_1210")

if __name__ == '__main__':
    input_path = "./input_data/traffic_accident.txt"
    output_path = "./output_data/traffic_accident_seg.txt"
    segment_file(input_path, output_path)
    my_model = train(output_path)
    # calc_similarity(my_model)
    # find_Correspondence(my_model)
    # find_twowords(my_model)
    find_different(my_model)
    save_model(my_model)