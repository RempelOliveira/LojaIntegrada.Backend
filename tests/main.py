from flask import Flask
from flask_restful import Api
from flask_mongoengine import MongoEngine

from dotenv import load_dotenv
from app.routes import load_routes


app = Flask(__name__)
app.config["MONGODB_HOST"] = "mongomock://localhost"

MongoEngine(app)


load_dotenv()
load_routes(Api(app))
