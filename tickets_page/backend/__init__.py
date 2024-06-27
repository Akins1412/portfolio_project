from backend.api import blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from backend.config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

cors = CORS()
cors.init_app(app)
jwt = JWTManager()
jwt.init_app(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app, model_class=Base)

app.register_blueprint(blueprint)
