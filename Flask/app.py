from flask import Flask, request, url_for, render_template
import flask_restplus
app = Flask(__name__)
api = flask_restplus.Api(app, prefix="/v1", title="Users", description="User CURD api")

@app.route('/users')
class UserApi(flask_restplus.Resource):
    def get(self):
        return {'users': '1'}

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return'''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
# def hello_world():
#     return 'Hello World!'

# 路由
# @app.route('/hello')
# def hello():
#     return 'Hello World'

# 变量规则
@app.route('/usr/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# 唯一url/重定向行为
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST"
    else:
        return "GET"

# 模板渲染
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# 环境局部变量
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

# 请求对象
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         print(request.form['username'])
#         print(request.form['password'])


if __name__ == '__main__':
    app.run()
