class Discount:
    def __init__(self, country, price, country_code):
        self.country = country
        self.price = price
        self.country_code = country_code

    def apply_discount(self):
        if self.country_code == "ES":
            return self.price * 0.2
        if self.country_code == "GB":
            return self.price * 0.4
        if self.country_code == "IT":
            return self.price * 0.3
