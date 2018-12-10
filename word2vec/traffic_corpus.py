#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import jieba
import os

# 1. 对于给定的语料库，首先要进行分词
def segment_file(read_path, write_path):
    # 1.1 判断路径是否存在
    if os.path.exists(read_path):
        with open(read_path, 'r', encoding='utf-8') as f:
            # f.readlines() 读取全部内容
            text = f.readlines()
            for line in text:
                line.replace('\t', '').replace('\n', '').replace(' ', '')
                seg_text = jieba.cut(line, cut_all=False)
                with open(write_path, 'w', encoding='utf-8') as f2:
                    f2.write(" ".join(seg_text))

if __name__ == '__main__':
    input_path = "./input_data/traffic_accident.txt"
    output_path = "./output_data/traffic_accident_seg.txt"
    segment_file(input_path, output_path)

