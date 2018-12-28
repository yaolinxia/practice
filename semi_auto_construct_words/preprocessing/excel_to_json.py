"""
时间：2018年12月25日
功能：完成电子表格到json的转换，每一行对应一个json
"""
import json
import xlrd


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
        words_list = []
        # for j in range(0, 2):
        # print(sh.cell_value(i, j))
        dict["code"] = int(sh.cell_value(i, 0))
        dict["action"] = sh.cell_value(i, 1)
        for s in sh.cell_value(i, 3).split(" "):
            if s:
                words_list.append(s)
        # 获取关键词的那一列，保存为一个列表
        dict["words"] = words_list
        dict_list.append(dict)
    # print(dict_list)
    return dict_list


# 对于words 进行处理，依次匹配json文件中的值，如果是，则加入,蛮力匹配
def match_words(words_list, words_dict):
    # 第一层遍历，获取每个列表
    for i in range(0, len(words_list)):
        # 第二层遍历。获取每个元素值
        for s in words_list[i]["words"]:
            if s in words_dict:
                # print(words_dict[s])
                words_list[i]["words"] = list(set(words_list[i]["words"] + words_dict[s]))
    print(words_list)
    return words_list
    # print(words_list[i]["words"])


def read_file(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    dict_text = eval(text)
    # print(text)
    return dict_text


def to_json(dict, save_path):
    with open(save_path, 'a', encoding='utf-8') as json_file:
        json.dump(dict, json_file, ensure_ascii=False)
        json_file.write('\n')


def to_json2(dict, save_path):
    with open(save_path, 'a', encoding='utf-8') as json_file:
        json.dumps(dict, ensure_ascii=False, sort_keys=True)
        json_file.write('\n')


if __name__ == '__main__':
    keyword_file = "E:\yaolinxia\\files\\南京违法行为关键词抽取_yao改.xlsx"
    json_path = "E:\yaolinxia\workspace\practice\practice\semi_auto_construct_words\models\output\\traffic_similarity_threshold_0.65_process.json"
    out_path = "./output/traffic_words2.json"
    # 返回的是一个list，每个元素都是一个dict
    json_excel_list = excel_to_json(keyword_file)
    words_dict = read_file(json_path)
    words_list = match_words(json_excel_list, words_dict)
    for c in words_list:
        to_json(c, out_path)
