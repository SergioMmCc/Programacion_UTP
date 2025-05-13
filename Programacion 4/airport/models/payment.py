class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def process_payment(self):
        # Logic to process payment
        print(f"Processing {self.method} payment of {self.amount}")