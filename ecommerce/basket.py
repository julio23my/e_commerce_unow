from .discount import Discount


class Basket:
    def __init__(self):
        self.items = []
        self.promotion_code = ''
        
    def __str__(self):
        return f'Basket with {len(self.items)} items'

    def add(self, product, quantity=1):
        repeat = False
        if self.items:
            for item in self.items:
                if item[0].name == product.name:
                    repeat = True
                    item[1] += quantity
                    return
        if not repeat:
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
            proudct_base_discount = self.find_base_discount(product.discount)
            if proudct_base_discount:
                price = self.apply_discount_to_total(product.price, proudct_base_discount)
                product_total += price * quantity
            else:
                product_total += product.price * quantity
            if product.discount:
                real_discount = self.find_my_real_discount(quantity, product.discount)
                if real_discount:
                    product_total = self.apply_discount_to_total(product_total, real_discount)
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
    
    @staticmethod
    def find_my_real_discount(quantity, discounts):
        if discounts:
            ordered_discounts = sorted(discounts, key=lambda d: d.quantity, reverse=True)
            for discount in ordered_discounts:
                if not discount.is_base and quantity >= discount.quantity:
                    return discount
        return None
    
    @staticmethod
    def find_base_discount(discounts):
        if discounts:
            for discount in discounts:
                if discount.is_base:
                    return discount
        return None
    
    @staticmethod
    def apply_discount_to_total(total, discount):
        if discount.is_percent:
            return total * discount.product_discount
        return total + discount.product_discount