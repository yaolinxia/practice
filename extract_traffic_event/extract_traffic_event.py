#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
任务描述：从给定的语料中挖掘事件
数据：交通事故问答语料库
事件：交通事件
输出：找出相应语料中对应的事件，尽可能多地枚举出事件; 存储到电子表格中，文件名就是event,内容是相应的语料

"""
import json
import re
import jieba
from xlwt import *


# 0. 读取语料库内容，当做一整个语料库
def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    return text


# 1. 读取事件，将它们存放在一个列表中，便于后续匹配;
# 1.1 定义函数：完成txt->list
def event_to_list(path):
    # 定义列表event_list存放事件
    event_list = []
    f = open(path, 'r', encoding='utf-8')
    for eachline in f:
        pattern = re.compile(r'[.、\n]')
        str = pattern.split(eachline)
        each_event = str[1]
        if each_event:
            each_event = each_event.strip()
            event_list.append(each_event)
        else:
            continue
    print(len(event_list))
    f.close()
    return event_list


# 1.2 将每个事件的序号也存进去
def event_to_list_nodel(path):
    # 定义列表event_list存放事件
    event_list = []
    f = open(path, 'r', encoding='utf-8')
    for eachline in f:
        event_list.append(eachline)
    print(len(event_list))
    # print(event_list)
    f.close()
    return event_list


# 1.3 匹配根节点
def f_event_to_list(path):
    # 定义列表f_event_list存放根事件
    f_event_list = []
    f = open(path, 'r', encoding='utf-8')
    for eachline in f:
        pattern = re.compile(r'[、]')
        str = pattern.split(eachline)
        if len(str) > 1:
            f_event_list.append("".join(str[1]).strip())
            # print("".join(str[1]))
    print(f_event_list)
    return f_event_list

# 1.4 匹配子节点
def s_event_to_list(path):
    # 定义列表s_event_list存放子事件
    s_event_list = []
    f = open(path, 'r', encoding='utf-8')
    for eachline in f:
        pattern = re.compile(r'[.]')
        str = pattern.split(eachline)
        if len(str) > 1:
            s_event_list.append("".join(str[1]).strip())
            # print("".join(str[1]))
    print(s_event_list)
    return s_event_list


# 1.5 返回根节点，子节点，层次结构{'超速': ['超速处罚', '超速扣分', '超速吊销驾驶证', '超速罚款']}
def fs_event_to_list(_list):
    # 定义列表s_event_list存放子事件
    fs_event_list = {}
    tmp = " "
    sub_list = []
    for i in range(0, len(_list)):
        # for j in range(i, len(_list)):
        if "、" in _list[i]:
            pattern = re.compile(r'[、]')
            str = pattern.split(_list[i])
            if len(str) > 1:
                tmp = "".join(str[1]).strip()
                sub_list = []
        if "." in _list[i]:
            pattern_sub = re.compile(r'[.]')
            str_sub = pattern_sub.split(_list[i])
            if len(str_sub) > 1:
                sub_list.append("".join(str_sub[1]).strip())
        if "\n" in _list[i]:
            # print("==========")
            fs_event_list[tmp] = sub_list
    print(fs_event_list)
    return fs_event_list

# 1.6 直接提取出主干事件,读取json文件
def extract_main_event(json_path):
    with open(json_path, 'r') as f:
        # 加载json
        load_dict = json.load(f)
    return load_dict



# 2. 将语料，每条问答语句，存储进list列表中
# 2.1 定义corpus_l存放每一条语料库
def corpus_to_list(corpus):
    corpus_l = []
    f = open(corpus, 'r', encoding="utf-8")
    for line in f:
        corpus_l.append(line)
    return corpus_l


# 3. 将语料库中的内容，与相应的事件进行匹配，如果符合就把事件提取出来,返回的结果是词典,最初的版本
def extract_event(event, corpus):
    # 3.1 定义一个字典event_corpus，存放事件-》语料（key:事件———>value:语料）; eg:["超速", [corpus1, corpus2]]
    event_corpus = {}
    # 3.2 先存放根事件，在对每条根事件e进行分词找寻子事件e_sub，再进行匹配
    for e in event:
        # 3.3 cut_all=False:非全模式(精确模式)； sub_corpus_l对应事件的所有匹配问答语句
        for e_sub in jieba.cut(e, cut_all=False):
            sub_corpus_l = []
            for each_corpus in corpus:
                # 3.4 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
                if (len(e_sub) == 1):
                    continue
                else:
                    # 3.5 匹配子事件
                    pattern_sub = re.compile(e_sub)
                    result_sub = pattern_sub.search(each_corpus)
                    # 3.6 如果子事件不为空，则将该条语句添加进sub_corpus_l列表，否则，继续
                    if result_sub:
                        sub_corpus_l.append(each_corpus)
                    else:
                        continue
        # 3.7 每条事件对应的问答语句，存放进词典event_corpus（key:事件———>value:语料）
        event_corpus[e] = sub_corpus_l
    print(len(event_corpus))
    return event_corpus


# 4. 只是提取事件，不需要相应的语料
def extract_event_only(event, corpus):
    # 定一个词典存放key:事件--》value:该事件出现的个数
    e_count = {}
    for e in event:
        e_count[e] = 0
    for e in event:
        # 4.1 匹配分词后的子事件,根事件也包含在其中
        for e_sub in jieba.cut(e, cut_all=False):
            for each_corpus in corpus:
                # 4.2 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
                if (len(e_sub) == 1):
                    continue
                else:
                    pattern_sub = re.compile(e_sub)
                    result_sub = pattern_sub.search(each_corpus)
                    # 4.3 如果匹配成功，词典中的结果加一
                    if result_sub:
                        e_count[e] += 1
                    else:
                        continue
    print(e_count)
    return e_count


# 4.4 只是提取事件，不需要相应的语料
def extract_event_format(f_event, s_event, corpus):
    # 定义一个词典e_count存放key:根事件，及其数量--》value:子事件词典（key:子事件——》value:数量）
    # eg: {[“超速”，2]:{"超速处罚": 6, "超速扣分": 123, "超速吊销驾驶证": 162, "超速罚款": 50}}
    # 合并存放根事件以及子事件
    fs_count = {}
    # 存放子事件
    s_count = {}
    # 所有的子事件的value初始化为0
    for e in s_event:
        s_count[e] = 0
    # 先考虑子事件，将子事件存储为词典形式
    for e in s_event:
        # 4.4.1 匹配分词后的子事件,根事件也包含在其中
        for e_sub in jieba.cut(e, cut_all=False):
            for each_corpus in corpus:
                # 4.4.2 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
                if (len(e_sub) == 1):
                    continue
                else:
                    pattern_sub = re.compile(e_sub)
                    result_sub = pattern_sub.search(each_corpus)
                    # 4.4.3 如果匹配成功，词典中的结果加一
                    if result_sub:
                        s_count[e] += 1
                    else:
                        continue

    print(s_count)
    return s_count


# 4.5 final_dict:{'超速': {'超速处罚':2, '超速扣分', '超速吊销驾驶证', '超速罚款'}}
# 可以存放相应事件的数量
def extract_event_format2(event_dict, corpus):
    # 定义一个新的词典，存放最终结果
    final_dict = {}
    # 需要定义每一个子词典
    # 先匹配根事件
    for f_event in event_dict:
        sub_dict = {}
        # 先考虑子事件，讲子事件存储为词典形式
        # 4.5.1 匹配分词后的子事件,根事件也包含在其中
        for i in range(0, len(event_dict[f_event])):
            for e_sub in jieba.cut(event_dict[f_event][i], cut_all=False):
                # 4.5.2 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
                for each_corpus in corpus:
                    if len(e_sub) == 1:
                        continue
                    else:
                        pattern_sub = re.compile(e_sub)
                        result_sub = pattern_sub.search(each_corpus)
                        # 如果匹配成功，词典中的结果加一
                        if result_sub:
                            sub_dict.setdefault(event_dict[f_event][i], 0)
                            sub_dict[event_dict[f_event][i]] += 1
                        else:
                            continue
        final_dict[f_event] = sub_dict
    return final_dict


# 4.6 event_dict:{'超速': ['超速处罚', '超速扣分', '超速吊销驾驶证', '超速罚款']}
# 将4.5的方法稍微做了一点点改进，词典中不存放词典，存放列表，并且不用计数
def extract_event_format3(event_dict, corpus):
    # 定义一个新的词典，存放最终结果
    final_dict = {}
    # 需要定义每一个子词典
    # 先匹配根事件
    for f_event in event_dict:
        sub_list = []
        # 先考虑子事件，讲子事件存储为词典形式
        # 4.1 匹配分词后的子事件,根事件也包含在其中
        for i in range(0, len(event_dict[f_event])):
            for e_sub in jieba.cut(event_dict[f_event][i], cut_all=False):
                # 4.2 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
                for each_corpus in corpus:
                    if len(e_sub) == 1:
                        continue
                    else:
                        pattern_sub = re.compile(e_sub)
                        result_sub = pattern_sub.search(each_corpus)
                        # 如果匹配成功，词典中的结果加一
                        if result_sub and event_dict[f_event][i] not in sub_list:
                            sub_list.append(event_dict[f_event][i])
                        else:
                            continue
        final_dict[f_event] = sub_list
    return final_dict

# 5. 将一个字典类型，转换到表格中，key值作为表格的名称，value值作为表格中的内容
# 5.1 *注意:file一定要在for循环外指定，否则每次都会生成一个file,之前创建的sheet会被覆盖
def dict_to_excel(dict, save_path):
    # 指定以utf-8格式打开
    file = Workbook(encoding='utf-8')
    for event_key in dict:
        # 5.2 指定打开的文件名：event_key（事件）
        table = file.add_sheet(event_key)
        for i, corpus_value in enumerate(dict[event_key]):
            table.write(i, 0, corpus_value)
    # 5.3 将电子表格保存到指定目录中save_path
    file.save(save_path)

# 6. 保存列表到电子表格中
def list_to_excel(list, save_path, save_name):
    file = Workbook(encoding='utf-8')
    table = file.add_sheet(save_name)
    for i, element in enumerate(list):
        table.write(i, 0, element)
    file.save(save_path)

# 7. 保存为json, 将词典格式保存为json
def to_json(dict, save_path):
    js_obj = json.dumps(dict, ensure_ascii=False)
    json_file = open(save_path, 'w')
    json_file.write(js_obj)
    json_file.close()

# 8. 保存为json, 将词典格式保存为json,另一种写法
def to_json2(dict, save_path):
    with open(save_path, 'a') as json_file:
        json.dump(dict, json_file, ensure_ascii=False, indent=2)
        json_file.write('\n')
        # js_obj = json.dumps(dict, ensure_ascii=False)
        # json_file = open(save_path, 'w')
        # json_file.write(js_obj)
        # json_file.close()

# 9. 单纯分割文本
def spilt_file(path):
    # a = open(path, 'r', encoding='utf-8')
    # file = a.read().splitlines()
    # file2 = a.read().split('\r\n')
    # for i in file2:
    #     print(i)
    #     print("++++++++++++++++++")
    # a.close()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
            print("---------------")

# 10. 不用匹配，直接将txt，转到txt文本中
# def txt_to_dict(event_dict, corpus):
#     # 定义一个新的词典，存放最终结果
#     final_dict = {}
#     # 需要定义每一个子词典
#     # 先匹配根事件
#     for f_event in event_dict:
#         sub_list = []
#         # 先考虑子事件，讲子事件存储为词典形式
#         # 4.1 匹配分词后的子事件,根事件也包含在其中
#         for i in range(0, len(event_dict[f_event])):
#             for e_sub in jieba.cut(event_dict[f_event][i], cut_all=False):
#                 # 4.2 过滤掉分词结果为1的，比如“有”，"在"等无意义单个字
#                 for each_corpus in corpus:
#                     if len(e_sub) == 1:
#                         continue
#                     else:
#                         pattern_sub = re.compile(e_sub)
#                         result_sub = pattern_sub.search(each_corpus)
#                         # 如果匹配成功，词典中的结果加一
#                         if result_sub and event_dict[f_event][i] not in sub_list:
#                             sub_list.append(event_dict[f_event][i])
#                         else:
#                             continue
#         final_dict[f_event] = sub_list
#     return final_dict

if __name__ == '__main__':
    corpus_path = "交通事故.txt"
    event_path = "traffic_event_add.txt"
    excel_path = "traffic_event_corpus.xlsx"
    json_path = "traffic_event.json"
    # total_corpus = read_file(corpus_path)
    """
    stage1:
    将事件提取出来，并且保存到json文件中
    """
    # corpus_list = corpus_to_list(corpus_path)
    # no_del_event = event_to_list_nodel(event_path)
    # event_corpus_dict = fs_event_to_list(no_del_event)
    # to_json2(event_corpus_dict, json_path)

    """
    stage2:
    读取json文件，并且提出相应的主干事件，读取dict的key值
    """
    json_path = "H:\python-workspace\qindun\extract_traffic_event\\traffic_event_final.json"
    json_dict = extract_main_event(json_path)
    for i in json_dict:
        print(i)
    # event_list = event_to_list(event_path)
    # f_event = f_event_to_list(event_path)
    # s_event = s_event_to_list(event_path)
    # fs_event = fs_event_to_list(event_path)

    # extract_event_format2(event_corpus_dict, corpus_list)
    # to_json2(extract_event_format3(event_corpus_dict, corpus_list), json_path)

    # dict_event_corpus = extract_event(event_list, corpus_list)
    # dict_to_excel(dict_event_corpus, excel_path)
    # list_to_excel(event_list)
    # to_json2(extract_event_only(event_list, corpus_list), json_path)
    # dict = {'Susan': ['1', '2'], 'Jone': ['3', '4'], 'Tom': ['5', '6']}
    # save_to_excel(dict)
    # spilt_file(event_path)
