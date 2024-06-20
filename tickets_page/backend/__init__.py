from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app=app, model_class=Base)
