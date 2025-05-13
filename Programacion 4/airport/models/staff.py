from person import Person

class Staff(Person):
    def __init__(self, name, age, charge):
        super().__init__(name, age)
        self.charge = charge

