# -*- coding: utf-8 -*-
# Created by igorwang on 2018/5/10

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from elasticsearch import Elasticsearch

from config.config import DATABASE_CONF

DB_TEXT = "mysql+pymysql://{user}:{passwd}@{h" \
          "ost}:{port}/{database}?charset=utf8mb4"


def get_session(db_name='mysql_test'):
    configs = DATABASE_CONF.get(db_name, None)
    if not configs:
        raise ValueError("NO SUCH DB NAMED WITH %s" % db_name)
    else:
        engine = create_engine(DB_TEXT.format(**configs))
    return sessionmaker(bind=engine)


def get_engine(db_name='mysql_test'):
    configs = DATABASE_CONF.get(db_name, None)
    if not configs:
        raise ValueError("NO SUCH DB NAMED WITH %s" % db_name)
    else:
        engine = create_engine(DB_TEXT.format(**configs))
    return engine


def get_es(db_name='es'):
    configs = DATABASE_CONF.get(db_name, None)
    if not configs:
        raise ValueError("NO SUCH DB NAMED WITH %s" % db_name)
    else:
        es = Elasticsearch(**configs)
    return es


if __name__ == '__main__':
    pass
