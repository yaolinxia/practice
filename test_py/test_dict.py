#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import openpyxl
from xlwt import *

dict = {'Susan': ['1', '2'], 'Jone': ['3', '4'], 'Tom': ['5', '6']}

# for i in dict.values():
#     print(i[0])
#
# for key in dict:
#     print(dict[key])
#     print(dict[key][0])

# 指定以utf-8格式打开
file = Workbook(encoding='utf-8')

for i, event_key in enumerate(dict):

    # 指定打开的文件名
    table = file.add_sheet(event_key)
    for i, corpus_value in enumerate(dict[event_key]):
        # print(corpus_value)
        table.write(i, 0, corpus_value)
#
# def save_excel(name):
#     for i in enumerate(dict[event_key]):
#         print(i)



file.save("1.xlsx")
print(dict)
#
# if __name__ == '__main__':
#     save_excel()



# 1. 读取语料库内容，当做一整个语料库
def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    return text


def test_re(text):
    print(repr(text))
    # re_words = re.compile(u"[\u4e00-\u9fa5]")
    re_words = re.compile(u"交通事故")
    print(re_words)
    m = re_words.search(text, 2)
    print(m.group())


def extract_event(event, corpus):
    # 定义一个字典，存放事件-》语料; eg:["超速", [corpus1, corpus2]]
    event_corpus = {}
    # 先存放根事件，在对根事件进行分词，再进行匹配
    for e in event:
        # 存放每一个事件所匹配的语句，key:事件———>value:语料
        corpus_l = []
        for each_corpus in corpus:
            pattern = re.compile(e)
            # 找根事件,看是否匹配
            result = pattern.search(each_corpus)
            # 如果不为空，添加进extract_e列表中
            if result and each_corpus:
                corpus_l.append(each_corpus)
            # print(corpus_l)
            sub_corpus_l = []
            for e_sub in jieba.cut(e, cut_all=False):
                if(len(e_sub) == 1):
                    continue
                else:
                    pattern_sub = re.compile(e_sub)
                    # 找子事件
                    result_sub = pattern_sub.search(each_corpus)
                    if result_sub:
                        sub_corpus_l.append(each_corpus)
            event_corpus[e_sub] = sub_corpus_l
        event_corpus[e] = corpus_l
    return event_corpus


# 2.2 因为需要尽可能匹配，对事件进行分词，扩大事件列表
# cut_all=True:全模式
def sentence_seg(sen, cut_all = False):
    sen = "我爱中华民族共和国"
    sen_cut = jieba.cut(sen, cut_all)
    # for i in sen_cut:
    #     print(i)
    # print(sen_cut)
    return sen_cut


def test():
    l = ["五、 无证驾驶", "五.无证驾驶"]
    if "." in l[0]:
        print("----")
    if "、" in l[0]:
        print("+++")

if __name__ == '__main__':
    test()
