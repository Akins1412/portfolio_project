from backend.models.base_model import BaseModel
from backend import db
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(db.Model, BaseModel):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    hash_password = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"Admin({self.username}, {self.email})"

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)
