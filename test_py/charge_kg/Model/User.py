import uuid

# 用户类
class User(object):
    user_id = None
    username = None

    def __init__(self, username:str):
        self.user_id = str(uuid.uuid4())
        self.username = username