from .discount import Discount


class Basket:
    def __init__(self):
        self.items = []
        self.promotion_code = ''

    def add(self, product, quantity, discount):
        self.items.append((product, quantity, discount))
        
    def apply_promotion_code(self, promotion_code, total):
        self.promotion_code = promotion_code
        if total > 90 and promotion_code == 'promo5':
            return total - 5
        if total > 200 and promotion_code == 'promo100':
            return total - 100
            
        
    def total(self):
        total = 0
        for product, quantity, discount in self.items:
            total += product.price * quantity
            if discount:
                total *= Discount.calculate_discount(country_code=product.country_code)
        return total

    def clean(self):
        self.items = []
