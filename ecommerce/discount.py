class Discount:
    def __init__(self, product_discount=0, is_percent=True, quantity=1, is_base=False):
        self.product_discount = product_discount
        self.quantity = quantity
        self.is_percent = is_percent
        if self.is_percent:
                self.product_discount = self.product_discount / 100 - 1
        else:
            self.product_discount = self.product_discount
        self.product_discount = self.product_discount * - 1
        self.is_base = is_base
        
    @staticmethod
    def calculate_discount_by_country(country_code) -> float:
        if country_code == "ES":
            return 1
        if country_code == "GB":
            return 0.9
        if country_code == "IT":
            return 0.75
        else:
            return 1
        
    @staticmethod
    def discount_by_quantity(quantity, price) -> float:
        if quantity > 10:
            return price - 5
        if quantity > 50:
            return price * 0.9
        if quantity > 200:
            return price * 0.8
        return price