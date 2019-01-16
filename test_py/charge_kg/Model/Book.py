import uuid

# 图书类
class Book(object):
    book_id = None
    book_name = None
    price = None

    def __init__(self, book_name:str, book_price:float):
        self.book_id = str(uuid.uuid4())
        self.book_name = book_name
        self.price = book_price