from flask import Flask
app = Flask(__name__)

def register_api():
    from apis.user_api import ns as user_api
    from apis.book_api import ns as book_api
    from apis.order_api import ns as order_api
    from apis import api
    api.add_namespace(book_api)
    api.add_namespace(order_api)

def create_app():
    app = Flask("Flask-Web-Demo")

    # register api namespace
    register_api()

    # register blueprint
    from apis.api import api_blueprint
    app.register_blueprint(api_blueprint)

    return app

if __name__ == '__main__':
    app.run()