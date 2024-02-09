class Basket:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        self.items.append((product, quantity))

    def total(self):
        return sum([product.price * quantity for product, quantity in self.items]) # E501

