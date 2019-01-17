# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/27
# ** Time: 13:39
from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields

api_v1 = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_v1, version='1.0', title='Todo API Demo', description='A simple TODO API')  # ,doc=False
# api = Api(api_v1, version='1.0', title='Todo API Demo', description='A simple TODO API', doc=False)

ns1 = api.namespace('todo_list', description='todo_list operations')  # namespace 1
ns2 = api.namespace('todos', description='todos operations')  # namespace 2

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

#  Output serializers
todo = api.model('Todo', {'task': fields.String(required=True, description='The task details'),
                          'name': fields.String(default='Anonymous User'), }
                 )

#  Output serializers
listed_todo = api.model('ListedTodo',
                        {
                            'id': fields.String(required=True, description='The todo ID'),
                            'todo': fields.Nested(todo, description='The Todo')
                        })


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        api.abort(404, "Todo {} doesn't exist".format(todo_id))

# Argument parsers
parser = api.parser()
parser.add_argument('task', required=True, help='The task details', location='json')


@ns1.route('/')
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @api.marshal_list_with(listed_todo)
    def get(self):
        """List all todos"""
        return [{'id': id, 'aaa': aaa} for id, aaa in TODOS.items()]

    @api.doc(parser=parser)
    @api.marshal_with(todo, code=201)
    @api.expect(todo)
    def post(self):
        """
        Create a todo
        """
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return {"xxx": "xxx"}, 201


@ns2.route('/<string:todo_id>')
@api.doc(responses={404: 'Todo not found'}, params={'todo_id': 'The Todo ID'})
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @api.doc(description='todo_id should be in {0}'.format(', '.join(TODOS.keys())))
    @api.marshal_with(todo)
    def get(self, todo_id):
        """Fetch a given resource"""
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    @api.doc(responses={204: 'Todo deleted'})
    def delete(self, todo_id):
        """Delete a given resource"""
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    @api.doc(parser=parser)
    @api.marshal_with(todo)
    def put(self, todo_id):
        """Update a given resource"""
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api_v1)
    app.run(port=5000, debug=True, threaded=True)
