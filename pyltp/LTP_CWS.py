#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import codecs

# from pyltp import SentenceSplitter
import pyltp
import os
model_path = "E:\YanJiuSheng-download\\2a\ltp_data_v3.4.0\ltp_data_v3.4.0"
cws_model = "E:\YanJiuSheng-download\\2a\ltp_data_v3.4.0\ltp_data_v3.4.0\cws.model"
pos_model = "E:\YanJiuSheng-download\\2a\ltp_data_v3.4.0\ltp_data_v3.4.0\pos.model"
ner_model = "E:\YanJiuSheng-download\\2a\ltp_data_v3.4.0\ltp_data_v3.4.0\\ner.model"
parser_model = "E:\YanJiuSheng-download\\2a\ltp_data_v3.4.0\ltp_data_v3.4.0\\parser.model"
from pyltp import Segmentor
from pyltp import SentenceSplitter
from pyltp import Postagger
from pyltp import NamedEntityRecognizer, Parser

# 分句子
def sen_spliter(sen):
    single_sen = SentenceSplitter.split(sen)
    print('\n'.join(single_sen))

# 分词
def sen_word(sen):
    # 初始化实例
    segmentor = Segmentor()
    # 加载LTP模型
    segmentor.load(cws_model)
    # 分词
    words = segmentor.segment(sen)
    print('\t'.join(words))
    # 转化成list输出
    words_list = list(words)
    # for word in words_list:
        # print(word)
    # 释放模型
    segmentor.release()
    return words_list

# 词性标注. words:已经切分好的词
def word_tag(words):
    # 初始化实例
    postagger = Postagger()
    # 加载模型
    postagger.load(pos_model)
    # 进行词性标注
    postags = postagger.postag(words)
    for word, tag in zip(words, postags):
        print(word+'/'+tag)
    # 释放模型
    postagger.release()
    return postags

# 命名实体识别,words:分词结果；postags:标注
def name_recognition(words, postags):
    # 初始化实例
    recognizer = NamedEntityRecognizer()
    # 加载模型
    recognizer.load(ner_model)
    netags = recognizer.recognize(words, postags)
    for word, ntag in zip(words, netags):
        print(word+'/'+ntag)
    # 释放模型
    recognizer.release()
    return netags

# 依存句法分析
def parse(words, postags):
    # 初始化实例
    parser = Parser()
    # 加载模型
    parser.load(parser_model)
    # 句法分析
    arcs = parser.parse(words, postags)
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    # 释放模型
    parser.release()

if __name__ == '__main__':
    sen = "你好，你觉得这个例子从哪里来的？当然还是直接复制官方文档，然后改了下这里得到的。"
    # sen_spliter(sen)
    words = sen_word(sen)
    tags = word_tag(words)
    name_recognition(words, tags)
    parse(words, tags)

