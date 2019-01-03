from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()


def print_doc():
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res['result'])

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    # print(doc)


# 创建es
def create_es():
    result = es.indices.create(index='news', ignore=400)
    print(result)


# 删除es
def delete_es():
    result = es.indices.delete(index='news', ignore=[400, 404])
    print(result)


# 插入数据
def insert_data():
    data = {
        'title': '美国留给伊拉克',
        'url': 'http://view.news.qq.com/index.htm',
    }
    result = es.create(index='news', doc_type='politics', id=1, body=data)
    print(result)


# 插入数据方法2
def insert_data2():
    data = {
        'title': '美国留给伊拉克',
        'url': 'http://view.news.qq.com/index.htm',
    }
    es.index(index='news', doc_type='politics', body=data)


def seg_sen():
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index='news', ignore=[400, 401])
    es.indices.create(index='news', ignore=400)
    result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)
    print(result)


# 数据部分
def data():
   datas = [
       {
           'title':"美国留给伊拉克的是个烂摊子吗",
           'url':"http:1//view.news.qq.com/zt2011/usa_iraq/index.htm",
           'data':"2011-12-16"
       },
       {
           'title': "美国留给伊拉克的是个烂摊子吗2",
           'url': "http:2//view.news.qq.com/zt2011/usa_iraq/index.htm",
           'data': "2011-12-17"
       },
       {
           'title': "美国留给伊拉克的是个烂摊子吗3",
           'url': "http:3//view.news.qq.com/zt2011/usa_iraq/index.htm",
           'data': "2011-12-18"
       },
       {
           'title': "美国留给伊拉克的是个烂摊子吗4",
           'url': "http:4//view.news.qq.com/zt2011/usa_iraq/index.htm",
           'data': "2011-12-19"
       },
   ]
   for data in datas:
       es.index(index='news', doc_type='politics', body=data)

   result = es.search(index='news', doc_type='politics')
   print(result)


if __name__ == '__main__':
    # print_doc()
    # create_es()
    # insert_data2()
    # delete_es()
    # seg_sen()
    data()
