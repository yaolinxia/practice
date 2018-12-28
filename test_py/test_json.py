#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import codecs

def med1():
    # 网上方法，测试下json读取文件
    json_path = "E:\yaolinxia\workspace\practice\practice\semi_auto_construct_words\models\output\\traffic_similarity_threshold_0.65.json"
    addrsfile = open(json_path, "r", encoding='utf-8')
    addrJson = json.loads(addrsfile)
    addrsfile.close()
    if addrJson:
        print("yes")

def med2(path):
    with open(path, encoding='utf-8') as f:
        line = f.read()
        d = json.loads(line)
        print(d)

def med3(path):
    data = []
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f.read():
            dic = json.load(line)
            data.append(eval(dic))
            print(json.dumps(dic, indent=4, ensure_ascii=False, encoding='utf-8'))

def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    dict_text = eval(text)
    # print(text)
    return dict_text

if __name__ == '__main__':
    json_path = "E:\yaolinxia\workspace\practice\practice\semi_auto_construct_words\models\output\\traffic_similarity_threshold_0.65_process.json"
    json_dict = read_file(json_path)
    print(json_dict)