class Flight:
    def __init__(self, flight_number, departure, arrival):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival

    def __repr__(self):
        return f"Flight({self.flight_number}, {self.departure}, {self.arrival})"