# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/25
# ** Time: 14:54
import warnings

from decimal import Decimal

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from os.path import join as path_join

import jieba.posseg as pseg
import numpy as np
from gensim.models import KeyedVectors
from sklearn.externals import joblib
from config.config import RESOURCE_DIR
from ml.charge_recognition import MODEL_PATH
from src.ml.save_load_method import load_model
from flask import Flask, request, jsonify
import operator
embedding_size = 300

model_path = path_join(MODEL_PATH, 'charges.model')

word2vec_path = path_join(RESOURCE_DIR, 'word2vec.bin')

label2index = load_model(MODEL_PATH, 'label2index.pkl')
index2label = load_model(MODEL_PATH, 'index2label.pkl')

word2vec = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

model = joblib.load(model_path)

def sentence2vec(sentence, use_word=True):
    if use_word:
        pos_filter = ['x', 'u', 'c', 'p', 'm', 't']
        word_list = [i.word for i in pseg.cut(sentence) if i.flag[0] not in set(pos_filter)]
    else:
        word_list = list(sentence)
    embedding = np.zeros(embedding_size)
    sentence_length = 0
    for idx, word in enumerate(word_list):
        if word in word2vec.vocab:
            embedding += word2vec.word_vec(word)
            sentence_length += 1
    return embedding / sentence_length


def predict(sentence):
    represent_sent = sentence2vec(sentence, use_word=False)
    text_vector = np.array(represent_sent).reshape(1, -1)
    label = index2label.get(model.predict(text_vector)[0])
    label_proba = model.predict_proba(text_vector)[0]

    result_dict = {}
    for i, p in enumerate(label_proba):
        p = float(p)
        p = float(Decimal(p).quantize(Decimal('0.0000')))  # 概率结果保留三位小数
        # if p > 0.35:
        #     result_dict[index2label[i]] = p
        result_dict[index2label[i]] = p
    result_dict = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))
    return  [label,result_dict]


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/', methods=["POST", "GET"])
def index():
    data = request.json
    sentence = data.get('sentence')
    represent_sent = sentence2vec(sentence,use_word=True)
    text_vector = np.array(represent_sent).reshape(1, -1)
    label = index2label.get(model.predict(text_vector)[0])
    label_proba = model.predict_proba(text_vector)[0]

    result_dict = {}
    for i, p in enumerate(label_proba):
        p = float(p)
        p = float(Decimal(p).quantize(Decimal('0.0000')))  # 概率结果保留三位小数
        # if p > 0.35:
        #     result_dict[index2label[i]] = p
        result_dict[index2label[i]] = p
    # result_dict = dict(sorted(result_dict.items(), key=lambda x: x[1],reverse=True))
    result_dict = dict(sorted(result_dict.items(), key=operator.itemgetter(1),reverse=True))
    print(result_dict)
    return jsonify(
        label=label,
        label_proba=result_dict
    )
    # entence = input("请输入：")
    # represent_sent = sentence2vec(sentence)
    # text_vector = np.array(represent_sent).reshape(1, -1)
    # label = index2label.get(model.predict(text_vector)[0])
    # label_proba = model.predict_proba(text_vector)[0]
    # print([label, label_proba])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5004", debug=True, threaded=False)
