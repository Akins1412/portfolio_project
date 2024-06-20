from backend.models.base_model import BaseModel
from datetime import datetime
from backend import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, BaseModel):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  hash_password = db.Column(db.String(120))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


  def __init__(self, username, email):
    self.email = email
    self.username = username

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.hash_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.hash_password, password)