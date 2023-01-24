import os
import json

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine

from debugger import debugger
from app.routes import load_routes


app = Flask(__name__)
app.config["MONGODB_HOST"] = f'{os.getenv("MONGODB_URL")}/{os.getenv("MONGODB_NAME")}'

if os.getenv("FLASK_DEBUGGER") == "True":
    debugger(os.getenv("FLASK_DEBUG_PORT"))

MongoEngine(app)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"error": str(e)}), e.code


load_routes(Api(app))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("FLASK_PORT"))
