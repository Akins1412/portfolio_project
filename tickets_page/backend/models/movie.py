from backend.models.base_model import BaseModel
from datetime import datetime
from backend import db


class Movie(db.Model, BaseModel):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    movie_fee = db.Column(db.Integer, nullable=False)

    # def __init__(self, title, release_date, description, rating)
    #   self.title = title
    #   self.release = release_date
    #   self.description = description
    #   self.rating = rating

    def __repr__(self):
        return '<Movie {}>'.format(self.title)


class Theater(db.Model, BaseModel):
    __tablename__ = "theaters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(80), unique=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    movies = db.relationship('Movie', backref='theater', lazy=True)

    def __init__(self, name, location):
        self.name = name
        self.location = location


class ShowTime(db.Model, BaseModel):
    __tablename__ = 'showtimes'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    showtime = db.Column(db.DateTime, nullable=False)
    theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'))
    movie = db.relationship(
        'Movie', backref=db.backref('showtimes', lazy='dynamic'))
    theater = db.relationship(
        'Theater', backref=db.backref('showtimes', lazy='dynamic'))

    def __init__(self, movie_id, showtime, theater_id):
        self.moive_id = movie_id
        self.showtime = showtime
        self.thater_id = theater_id

    def __repr__(self):
        return '<ShowTime {}>'.format(self.showtime)


class Booking(db.Model, BaseModel):

    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    showtime_id = db.Column(db.Integer, db.ForeignKey('showtimes.id'))
    seats = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    user = db.relationship(
        'User', backref=db.backref('bookings', lazy='dynamic'))
    showtime = db.relationship(
        'ShowTime', backref=db.backref('bookings', lazy='dynamic'))

    def __init__(self, user_id, showtime_id, seats, booking_date):
        self.user_id = user_id
        self.showtime_id = showtime_id
        self.seats = seats
        self.booking_date = booking_date

    def __repr__(self):
        return '<Booking {}>'.format(self.booking_date)
