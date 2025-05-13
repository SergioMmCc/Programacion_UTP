from passenger import Passenger
from flight import Flight
class Booking:
    def __init__(self, passenger: Passenger, flight: Flight):
        self.passenger = passenger
        self.flight = flight

    def __repr__(self):
        return f"Booking({self.passenger}, {self.flight})"