from flask_restplus import Resource, fields, Namespace

from Model import Order, Book, User
from apis.user_api import user_model
from apis.book_api import book_model

ns = Namespace("order", description="Order CURD api.")

order_model = ns.model('OrderModel', {
    "order_id": fields.String(readOnly=True, description='The order unique identifier'),
    "user": fields.Nested(user_model, description='The order creator info'),
    "book": fields.Nested(book_model, description='The book info.'),
    "created_at": fields.Integer(readOnly=True, description='create time: unix timestamp.'),
})
order_list = ns.model('OrderListModel', {
    "orders": fields.List(fields.Nested(order_model)),
    "total": fields.Integer(description='len of orders')
})

book = Book("Book1", 10.5)
user = User("LiLei")
order = Order(user.user_id, book.book_id)


@ns.route("")
class UserListApi(Resource):

    @ns.doc('get_order_list')
    @ns.marshal_with(order_list)
    def get(self):
        return {
            "orders": [{
                "order_id": order.order_id,
                "created_at": order.created_at,
                "user": {
                    "user_id": user.user_id,
                    "username": user.username,
                },
                "book": {
                    "book_id": book.book_id,
                    "book_name": book.book_name,
                    "price": book.price,
                }
            }],
            "total": 1}

    @ns.doc('create_order')
    @ns.expect(order_model)
    @ns.marshal_with(order_model, code=201)
    def post(self):
        return {
            "order_id": order.order_id,
            "created_at": order.created_at,
            "user": {
                "user_id": user.user_id,
                "username": user.username,
            },
            "book": {
                "book_id": book.book_id,
                "book_name": book.book_name,
                "price": book.price,
            }
        }
