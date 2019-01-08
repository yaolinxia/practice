# from .main import main as main_blueprint
#
# app.register_blueprint(main_blueprint)
#
# from .auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint, url_prefix='/auth')

from flask import Flask
# from .main.simple_page import simple_page
from .main import simple_page as simple_page
app = Flask(__name__)
app.register_blueprint(simple_page,url_prefix='/pages')
print("simple_page.root_path", simple_page.root_path)
with simple_page.open_resource('static/style.css') as f:
    code = f.read()
# if __name__ == '__main__':
#     app.run()
