from flask_restplus import Resource, fields, Namespace

from Model import User
from apis import api

ns = Namespace("users", description="Users CURD api.")

# 创建user model 让Flask-Restplus 知道如何渲染和解析json
user_model = ns.model('UserModel', {
    'user_id': fields.String(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})
user_list_model = ns.model('UserListModel', {
    'users': fields.List(fields.Nested(user_model)),
    'total': fields.Integer,
})


@ns.route("")
class UserListApi(Resource):
    # 初始化数据
    users = [User("HanMeiMei"), User("LiLei")]
    # ns.doc 标记api的作用
    @ns.doc('get_user_list')
    # ns.marshal_with 标记如何渲染返回的json
    @ns.marshal_with(user_list_model)
    def get(self):
        return {
            "users": self.users,
            "total": len(self.users),
        }

    @ns.doc('create_user')
    # ns.expect 来标记我们预期什么样子的 request
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        user = User(api.payload['username'])
        return user