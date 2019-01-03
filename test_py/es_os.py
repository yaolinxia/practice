import json
import os
import sys
import time
import urllib3

class importEsData():
    def __init__(self, url, index, type):
        self.url = url+'/'+index+'/'+type
        self.index = index
        self.type = type

    def post(self, data):
        req = urllib3.request(self.url, data, {"Content-Type":"application/json; charset=UTF-8"})
        urllib3.connection(req)

    def importData(self):
        print("import data begin")
        begin = time.time()
        f = open(self.index + '_' + self.type + '.json', 'r')
        try:
            for line in f:
                self.post(line)
        finally:
            f.close()
        print("import data end!!\n\t total consuming time:"+str(time.time()-begin)+'s')

if __name__ == '__main__':
    # importEsData("http://localhost:9200", "test", "3").importData()
    name = "未取得机动车驾驶证驾驶非营运汽车的"
    li = ["影响通行", "法规规定", "拒不改正"]
    l1 = []
    l1.append(name)
    str = l1+li
    print(str)
