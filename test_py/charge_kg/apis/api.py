from flask import Blueprint
from flask_restplus import Api

api_blueprint = Blueprint("open_api", __name__, url_prefix="/api")
api = Api(api_blueprint, version="1.0",
          prefix="/v1", title="OpenApi", description="The Open Api Service")