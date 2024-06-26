from flask_restx import Namespace, Resource
from http import HTTPStatus

booking_api = Namespace("bookings", description="Return all bookings")


@booking_api.route("/")
class Get_Booking(Resource):
    def get(self):
        from backend.models.movie import Booking

        """Return all bookings"""
        bookings = Booking.query.all()
        if not bookings:
            return "No bookings available"
        return [{booking.id: booking.to_json()} for booking in bookings], HTTPStatus.OK


@booking_api.route("/<int:booking_id>")
class Get_Booking(Resource):
    def get(self, booking_id):
        from backend.models.movie import Booking

        """Return a booking"""
        booking = Booking.query.get(booking_id)
        if not booking:
            return "No bookings available"
        return {booking.id: booking.to_json()}, HTTPStatus.OK
