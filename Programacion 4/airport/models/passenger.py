from .person import Person
class Passenger(Person):
    def __init__(self, name, age, passport, chair):
        super().__init__(name, age)
        self.passport = passport
        self.chair = chair
