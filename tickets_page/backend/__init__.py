from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from backend.config import Config
from backend.api import blueprint

app = Flask(__name__)
app.config.from_object(Config)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)
app.register_blueprint(blueprint)
