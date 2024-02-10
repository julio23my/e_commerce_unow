class Discount:
    def __init__(self):
        pass

    def calculate_discount(self, country_code) -> float:
        if country_code == "ES":
            return 1
        if country_code == "GB":
            return 0.9
        if country_code == "IT":
            return 0.75
        else:
            return 1
    
    def discount_by_quantity(self, quantity, price) -> float:
        if quantity > 10:
            return price - 5
        if quantity > 50:
            return price * 0.9
        if quantity > 200:
            return price * 0.8
        return price