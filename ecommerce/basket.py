from .discount import Discount


class Basket:
    def __init__(self):
        self.items = []
        self.promotion_code = ''
        
    def __str__(self):
        return f'Basket with {len(self.items)} items'

    def add(self, product, quantity=1):
        self.items.append((product, quantity))
        
    def apply_promotion_code(self, promotion_code):
        self.promotion_code = promotion_code
        
    def apply_promotion_code_total(self, total):
        self.promotion_code
        if total > 90 and self.promotion_code == 'promo5':
            return total - 5
        if total > 200 and self.promotion_code == 'promo100':
            return total - 100
        else:
            return total
            
        
    def total_before_promotion_code(self):
        total = 0
        for product, quantity in self.items:
            product_total = 0
            product_total += product.price * quantity
            if product.discount:
                product_total *= product.discount
            if product.country_code:
                product_total *= Discount.calculate_discount_by_country(country_code=product.country_code)
            total += product_total
        return total
    
    def total_after_promotion_code(self):
        total = self.total_before_promotion_code()
        return self.apply_promotion_code_total(total)
    
    def total(self):
        return self.total_after_promotion_code()
    
    def clean(self):
        self.items = []
        self.promotion_code = ''

    def get_total_items(self):
        total = 0
        for product, quantity in self.items:
            total += quantity
        return total