import os
import json

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_httpauth import HTTPBasicAuth

from prometheus_flask_exporter import RESTfulPrometheusMetrics

from debugger import debugger
from app.routes import load_routes


app = Flask(__name__)
app.config["MONGODB_HOST"] = f'{os.getenv("MONGODB_URL")}/{os.getenv("MONGODB_NAME")}'

restful_api = Api(app)


if os.getenv("FLASK_DEBUG") == "True":
    debugger(os.getenv("FLASK_DEBUG_PORT"))

CORS(app, resources={r"/*": {"origins": "*"}})
MongoEngine(app)

metrics_auth = \
    HTTPBasicAuth()

RESTfulPrometheusMetrics(app, restful_api, path="/metrics", metrics_decorator=metrics_auth.login_required)


@metrics_auth.verify_password
def verify_credentials(username, password):
    return (username, password) == ("user", "pass")

@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"error": str(e)}), e.code


load_routes(restful_api)


if __name__ == "__main__":
    app.run(host=os.getenv("FLASK_RUN_HOST"), port=os.getenv("FLASK_RUN_PORT"))
