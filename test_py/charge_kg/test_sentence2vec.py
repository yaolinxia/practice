from gensim.models import KeyedVectors
import jieba.posseg as pseg
import numpy as np
from tqdm import tqdm
import json
# from . import save_load_method
from save_load_method import save_model, load_model
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

word2vec_path = "E:\yaolinxia\\files\word2vec.bin"
train_file = "E:\yaolinxia\workspace\practice\practice\semi_auto_construct_words\preprocessing\output\\traffic_words_new.json"
word2vec = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)
embedding_size = 300

# 为每一句话，定义词向量，句子的向量表示，是每一个词向量表示的累加和
def sentence2vec(sentence, use_word=True):
    # 过滤掉下面这些词性
    if use_word:
        pos_filter = ['x', 'u', 'c', 'p', 'm', 't']
        word_list = [i.word for i in pseg.cut(sentence) if i.flag[0] not in set(pos_filter)]
    else:
        word_list = list(sentence)
    # print(word_list)
    embedding = np.zeros(embedding_size)
    # print(embedding)
    sentence_length = 0
    for idx, word in enumerate(word_list):
        if word in word2vec.vocab:
            # print(word)
            # word2vec.word_vec ：打印出词向量
            embedding += word2vec.word_vec(word)
            # print(embedding)
            sentence_length += 1
    # print(embedding)
    return embedding / sentence_length

# train_x中存储的是一个个的句子的向量表示
# trian_y中存放的是标签
label2index = {}
def processing_data():
    train_x = []
    train_y = []
    with open(train_file, 'r', encoding='utf-8') as f:
        count = 0
        for line in tqdm(f):
            count += 1
            data = json.loads(line)
            label = data.get('code')
            label_id = label2index.get(label)
            print(label_id)
            sent = sentence2vec(data.get('action'), use_word=True)
            train_x.append(sent)
            train_y.append(label_id)
            # 每1000个输出一下
            if count % 10000 == 0:
                print('loaded %s lines' % count)
    save_model("./output", 'train_x.pkl', train_x)
    save_model("./output", 'train_y.pkl', train_y)

def train_model(test_size=0.1, shuffle=True):
    train_x = load_model("./output", 'train_x.pkl')
    train_y = load_model("./output", 'train_y.pkl')
    # 看是否打乱
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
    # joblib.dump(model, model_path)


if __name__ == '__main__':
    sentence = "与上一样，也是产生迭代器，但需要更改下文件格式。简单的格式：一句话=一行; 单词已经过预处理并由空格分隔。"
    # sentence2vec(sentence)
    processing_data()