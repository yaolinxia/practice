# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/21
# ** Time: 17:31
import hashlib
import string
import uuid

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

def get_uuid() -> str:
    """
    生成唯一id
    :return: str
    """
    ALPHA = string.ascii_letters
    while True:
        rst = str(uuid.uuid4())
        if rst.startswith(tuple(ALPHA)):
            return rst
