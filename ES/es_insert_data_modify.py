# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/16
# ** Time: 11:21
import json
import logging

logging.getLogger().setLevel(logging.INFO)
import hashlib

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
config = {
    "timeout": 60,
    "type": "es",
    "http_auth": [
        "aegis",
        "shield"
    ],
    "hosts": [
        "117.78.26.103:9200",
        "117.78.26.208:9200"
        # "localhost:9200"
    ]
}

def get_md5(string) -> str:
    """
    根据字符串生成md5
    :param string:
    :return:
    """
    if isinstance(string, str):
        string = string.encode("utf-8")
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()

es = Elasticsearch(**config)

query_params = {
    "query": {
        "bool": {
            "must": [

            ],
            "should": [

            ]
        }
    }
}

def import_picklaw_kg_search_v1(index_name, doc_type_name):
    current_index = 1
    bulk_batch_size = 2000  # 2000条为一批
    load_data = []
    with open('picklaw_kg_search_v1.json','r',encoding='utf-8') as f:
        for line in f:
            current_index +=1
            line = json.loads(line)
            entity = line.get('entity')
            line['is_enable'] = 1
            if entity:
                obj = {
                    "_index": index_name,
                    "_type": doc_type_name,
                    "_id": get_md5(entity),
                    "_source": line,
                    "doc_as_upsert": True,
                }

                load_data.append(obj)
                if len(load_data) == bulk_batch_size:
                    print('插入', int(current_index / bulk_batch_size), '批数据')
                    success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
                    del load_data[0:len(load_data)]
                    print(success, failed)
    if len(load_data) > 0:
        success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
        del load_data[0:len(load_data)]
        print(success, failed)

def import_sa_corpus_search_v1_1(index_name, doc_type_name):
    current_index = 1
    bulk_batch_size = 2000  # 2000条为一批
    load_data = []
    with open('./data/traffic_words_new.json', 'r', encoding='utf-8') as f:
        for line in f:
            current_index += 1
            str_list = []
            data = json.loads(line)
            # id = data.get('id')
            action = data.get("action")
            str_list.append(action)
            code = data.get("code")
            words = data.get("words")
            # laws_dict = data.get("laws_dict")
            data_record = dict(
                # id=id,
                action_name=action,
                code=code,
                action_search=str_list + words,
            )
            obj = {
                "_index": index_name,
                "_type": doc_type_name,
                # "_id": id,
                "_source": data_record,
                "doc_as_upsert": True,
            }
            load_data.append(obj)
            if len(load_data) == bulk_batch_size:
                print('插入', int(current_index / bulk_batch_size), '批数据')
                success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
                del load_data[0:len(load_data)]
                print(success, failed)
    if len(load_data) > 0:
        success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
        del load_data[0:len(load_data)]
        print(success, failed)
        # if len(load_data) > 0:
        #     success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
        #     del load_data[0:len(load_data)]
        #     print(success, failed)
        #
        #     if laws_dict:
        #         data_record = dict(
        #             id=id,
        #             answer=answer,
        #             domain=domain,
        #             is_enable=is_enable,
        #             question=question,
        #             update_timestame=update_timestamp,
        #             laws_nested=[ dict(
        #                 law_clause=item.get('law_clause'),
        #                 law_name=item.get('law_name'),
        #                 law_content=item.get('content')
        #             ) for item in laws_dict]
        #         )
        #         # print(data_record)
        #         # input()
        #         obj = {
        #             "_index": index_name,
        #             "_type": doc_type_name,
        #             "_id": id,
        #             "_source": data_record,
        #             "doc_as_upsert": True,
        #         }
        #     #
        #         load_data.append(obj)
        #         if len(load_data) == bulk_batch_size:
        #             print('插入', int(current_index / bulk_batch_size), '批数据')
        #             success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
        #             del load_data[0:len(load_data)]
        #             print(success, failed)
    if len(load_data) > 0:
        success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
        del load_data[0:len(load_data)]
        print(success, failed)

if __name__ == '__main__':
    # import_picklaw_kg_search_v1('picklaw_kg_search_v1','_doc')
    import_sa_corpus_search_v1_1('traffic_illegal_action_nj','_doc')
    # result = es.search(index='traffic_illegal_action_nj')
    # print(result)
    # es.indices.delete(index='traffic_illegal_action_nj')
    # index_name = 'sa_corpus_search_v1_1'
    # doc_type_name = '_doc'
    #
    # current_index = 1
    # bulk_batch_size = 2000  # 2000条为一批
    # load_data = []
    # with open('./劳动争议.json', 'r', encoding='utf-8') as f:
    #     for line in f:
    #         data = json.loads(line)
    #         answer = data.get("answer")
    #         domain = data.get("domain")
    #         is_enable = data.get("is_enable")
    #         update_timestamp = data.get("update_timestamp")
    #         laws = data.get("laws")
    #         laws_nested = data.get("laws_nested")
    #         question_list = data.get("question_list")
    #         if len(question_list) > 0:
    #             for question in question_list:
    #                 current_index += 1
    #                 id = get_md5(question)
    #                 data_record = dict(
    #                     id=id,
    #                     answer=answer,
    #                     domain=domain,
    #                     is_enable=is_enable,
    #                     question=question,
    #                     update_timestame=update_timestamp,
    #                     laws_nested=laws_nested
    #                 )
    #                 # print(data_record)
    #
    #                 obj = {
    #                     "_index": index_name,
    #                     "_type": doc_type_name,
    #                     "_id": id,
    #                     "_source": data_record,
    #                     "doc_as_upsert": True,
    #                 }
    #                 #
    #                 load_data.append(obj)
    #
    #                 if len(load_data) == bulk_batch_size:
    #                     print('插入', int(current_index / bulk_batch_size), '批数据')
    #                     success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
    #                     del load_data[0:len(load_data)]
    #                     print(success, failed)
    # if len(load_data) > 0:
    #     success, failed = bulk(es, load_data, index=index_name, raise_on_error=False)
    #     del load_data[0:len(load_data)]
    #     print(success, failed)
