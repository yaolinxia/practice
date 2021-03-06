#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import gensim
import codecs
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import logging
import json
import xlrd

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

# 5. 计算两个词的相关词列表,key为word，value为概率值
def find_twowords(my_model, word):
    # y = my_model.most_similar(u"交通事故", topn=20)
    sub_str_dict = {}
    if word in my_model:
        y = my_model.most_similar(word, topn=20)
        # print("和%s相关的词有：" % word)
        for item in y:
            # print(item[0], item[1])
            sub_str_dict[item[0]] = item[1]
    str_dict[word] = sub_str_dict
    # print(str_dict)
    return str_dict

# 5.1 计算两个词的相关词列表,只保存词，不保存概率，将词保存到列表中
def find_twowords_only_word(my_model, word, threshold):
    sub_str_list = []
    if word in my_model:
        y = my_model.most_similar(word, topn=20)
        # print("和%s相关的词有：" % word)
        for item in y:
            if item[1] >= threshold:
                # print(item[0], item[1])
                sub_str_list.append(item[0])
    # print(str_dict)
    return sub_str_list

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
    return gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    # return gensim.models.Word2Vec.load(model_path)

# 9. 读取文件，并且保存为列表
def read_file(file_path):
    # 定义一个存放事件的列表
    event = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            event.append(''.join(line).strip())
    print(event)
    return event

# 读数据
def read_excel(path):
    # 定义一个列表，存放关键词
    keyword = []
    bk = xlrd.open_workbook(path)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("工作表1")
    except:
        print("代码出错")
    # 获取行数
    nrows = sh.nrows
    for i in range(1, nrows):
        for s in sh.cell_value(i, 3).split(" "):
            if s and s not in keyword:
                keyword.append(s)
        # print(sh.cell_value(i, 3))
    # print(keyword)
    return keyword

# 将电子表格中的值，转成json格式，每一行对应一个json
def excel_to_json(path):
    # 定义一个列表，存放所有的dict
    dict_list = []
    bk = xlrd.open_workbook(path)
    try:
        sh = bk.sheet_by_name("工作表1")
    except:
        print("代码出错")
    # 获取行数
    nrows = sh.nrows
    # 每一行都是一个dict,每一行新开一个dict
    for i in range(1, nrows):
        dict = {}
        # for j in range(0, 2):
        # print(sh.cell_value(i, j))
        dict["code"] = sh.cell_value(i, 0)
        dict["action"] = sh.cell_value(i, 1)
        # 获取关键的那一列
        dict["words"] = sh.cell_value(i, 3)
        dict_list.append(dict)
    print(dict_list)
    return dict_list

if __name__ == '__main__':
    # 分词之后的结果
    # input_path = "F:\pycharm\yao\out_3.txt"
    # segment_file(input_path, output_path)
    keyword_file = "E:\yaolinxia\\files\\南京违法行为关键词抽取_yao改.xlsx"
    key_file = ""
    model_path = "E:\yaolinxia\\files\word2vec.bin"
    json_path = "E:\yaolinxia\workspace\practice\practice\semi_auto_construct_words\models\output\\traffic_similarity_threshold_0.6.json"
    my_model = load_model(model_path)
    print("load model successful")
    str_dict = {}

    # read json 文件
    # read_json(json_path)
    # str_list = read_file(input_path)
    # 读取原电子表格文件
    key_list = read_excel(keyword_file)
    print(key_list)
    # json_excel_list:存储每一行
    json_excel_list = excel_to_json(keyword_file)
    # 将关键词那一列加入列表中的每一个dict
    # for i in range(0, len(key_list)):
    #     str_list = find_twowords_only_word(my_model, key_list, 0.65)


    # 寻找相似词
    for s in key_list:
        str_list = find_twowords_only_word(my_model, s, 0.6)
        if len(str_list):
            str_dict[s] = str_list
    print(str_dict)
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
