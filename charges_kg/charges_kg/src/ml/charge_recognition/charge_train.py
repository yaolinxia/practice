# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/25
# ** Time: 14:54

import json
import warnings
from os.path import join as path_join

from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import jieba.posseg as pseg
import numpy as np
from gensim.models import KeyedVectors
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from ...config.config import RESOURCE_DIR
from ...ml.charge_recognition import MODEL_PATH
from ....src.ml.save_load_method import save_model, load_model

embedding_size = 300

model_path = path_join(MODEL_PATH, 'charges.model')

word2vec_path = path_join(RESOURCE_DIR, 'word2vec.bin')

train_file = path_join(MODEL_PATH, 'train.json')

label2index = {}

with open(path_join(MODEL_PATH, 'charges.txt'), 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        line = line.strip()
        label2index[line] = idx

index2label = {v: k for k, v in label2index.items()}

save_model(MODEL_PATH, 'label2index.pkl', label2index)
save_model(MODEL_PATH, 'index2label.pkl', index2label)

word2vec = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

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


def processing_data():
    train_x = []
    train_y = []
    with open(train_file, 'r', encoding='utf-8') as f:
        count = 0
        for line in tqdm(f):
            count += 1
            data = json.loads(line)
            label = data.get('charges')
            label_id = label2index.get(label)
            sent = sentence2vec(data.get('fact'), use_word=True)
            train_x.append(sent)
            train_y.append(label_id)
            if count % 10000 == 0:
                print('loaded %s lines' % count)
    save_model(MODEL_PATH, 'train_x.pkl', train_x)
    save_model(MODEL_PATH, 'train_y.pkl', train_y)


def train_model(test_size=0.1, shuffle=True):
    train_x = load_model(MODEL_PATH, 'train_x.pkl')
    train_y = load_model(MODEL_PATH, 'train_y.pkl')
    if shuffle:
        shuffle_indices = np.random.permutation(np.arange(len(train_y)))
        train_x = np.array(train_x)
        train_y = np.array(train_y)
        train_x_shuffle = train_x[shuffle_indices]
        train_y_shuffle = train_y[shuffle_indices]
        train_x, test_x, train_y, test_y = train_test_split(train_x_shuffle, train_y_shuffle, test_size=test_size)
    else:
        train_x, test_x, train_y, test_y = train_test_split(train_x, train_y, test_size=test_size)
    # model = LinearSVC(verbose=1)
    model = CalibratedClassifierCV(
        base_estimator=LinearSVC(verbose=1),
        method='sigmoid', cv=2
    )
    model.fit(train_x, train_y)
    joblib.dump(model, model_path)

    pred_Y = model.predict(np.array(test_x))
    accuracy = accuracy_score(y_true=test_y, y_pred=pred_Y)
    print("precision on test:{}".format(accuracy))

    # confusion_matrix(test_y, pred_X)

    y_predict = model.predict(train_x)
    all = len(y_predict)
    right = 0
    for i in range(len(train_y)):
        y = train_y[i]
        y_pred = y_predict[i]
        if y_pred == y:
            right += 1
    print('precision on train:%s/%s=%s' % (right, all, right / all))


def predict(sentence):
    model = joblib.load(model_path)
    represent_sent = sentence2vec(sentence)
    text_vector = np.array(represent_sent).reshape(1, -1)
    res = model.predict(text_vector)[0]
    label = label2index.get(res)
    return label


if __name__ == '__main__':
    # processing_data()

    # train_model()

    model = joblib.load(model_path)
    while True:
        sentence = input("请输入：")
        represent_sent = sentence2vec(sentence)
        text_vector = np.array(represent_sent).reshape(1, -1)
        label = index2label.get(model.predict(text_vector)[0])
        label_proba = model.predict_proba(text_vector)[0]
        print([label, label_proba])
