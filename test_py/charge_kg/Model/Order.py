import uuid
import time

# 订单
class Order(object):
    order_id = None
    user_id = None
    book_id = None
    created_at = None

    def __init__(self, user_id, book_id):
        self.order_id = str(uuid.uuid4())
        self.user_id = user_id
        self.book_id = book_id
        self.created_at = int(time.time())