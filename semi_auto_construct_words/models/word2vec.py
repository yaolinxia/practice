#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import gensim
import codecs
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import logging
import json

# 训练word2vec模型， 构建模型
def train(path):
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
    # 加载语料
    sentences = word2vec.Text8Corpus(path)
    # 训练skip-gram模型， 默认windows=5
    model = word2vec.Word2Vec(sentences, size=200)
    # print(model)
    # try:
    #     y1 = model.similarity(u"国家", u"国务院")
    # except KeyError:
    #     y1 = 0
    # print("国家，国务院的相似度为：", y1)
    return model

# 2. 寻找形似词
def get_similar_words_str(key_words, model, topn=10):
    result_words = get_similar_words_list(key_words, model)
    return str(result_words)


def get_similar_words_list(key_words, model, topn=10):
    result_words = []
    try:
        similary_words = model.most_similar(key_words, topn=10)
        print(similary_words)
        for (word, similarity) in similary_words:
            result_words.append(word)
        print(result_words)
    except:
        print("There are some errors!" + key_words)
    return result_words

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
    y = my_model.most_similar([u'交通事故', u'交通规则'], [u'违反交通'], topn=3)
    for item in y:
        print(item[0], item[1])

str_dict = {}
# 5. 计算两个词的相关词列表
def find_twowords(my_model, word):
    # y = my_model.most_similar(u"交通事故", topn=20)
    sub_str_dict = {}
    if word in my_model:
        y = my_model.most_similar(word, topn=20)
        print("和%s相关的词有：" % word)
        for item in y:
            print(item[0], item[1])
            sub_str_dict[item[0]] = item[1]
    str_dict[word] = sub_str_dict
    # print(str_dict)
    return str_dict

# 5.2. 保存为json, 将词典格式保存为json,另一种写法
def to_json(dict, save_path):
    with open(save_path, 'a', encoding='utf-8') as json_file:
        json.dump(dict, json_file, ensure_ascii=False, indent=2)
        json_file.write('\n')

# 6. 寻找不合群的词
def find_different(my_model):
    y = my_model.doesnt_match(u"交通 肇事 罪名 很".split())
    print("不合群的词：", y)

# 7. 保存模型，便于以后重用
def save_model(my_model):
    my_model.save("my_model_1220")

# 8. 加载模型
def load_model(model_path):
    print("load model")
    return gensim.models.Word2Vec.load(model_path)

# 9. 读取文件，并且保存为列表
def read_file(file_path):
    # 定义一个存放事件的列表
    event = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            event.append(''.join(line).strip())
    print(event)
    return event

if __name__ == '__main__':
    # 分词之后的结果
    input_path = "H:\python-workspace\pyltp\out_3.txt"
    # segment_file(input_path, output_path)
    key_file = ""
    model_path = "my_model_1220"
    json_path = "str_similarity2.json"
    my_model = load_model(model_path)
    print("load model successful")
    str_list = read_file(input_path)
    # 寻找相似词
    for s in str_list:
        str_dict = find_twowords(my_model, s)
    to_json(str_dict, json_path)
    # words = get_similar_words_str('交通', my_model)
    # print(words)
    # 构建模型
    # my_model = train(input_path)
    # calc_similarity(my_model)
    # find_Correspondence(my_model)
    # find_twowords(my_model)
    # find_twowords(my_model, '交通事故')
    # find_different(my_model)
    # save_model(my_model)
