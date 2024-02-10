class Product:
    def __init__(self, name, price, country_code=''):
        """product class create

        Args:
            name (str): name of the product
            price (int): price of the product
            country_code (str, optional): Country of the product this can be in multiple countries.
                                    Defaults to '' that means is a global price.
        """
        self.name = name
        self.price = price
        self.country_code = country_code.upper()

    def __str__(self):
        country = self.country_code if self.country_code else 'Global'
        return f"{self.name} - {self.price} - {country}"


def make_product(name, price, country_code=''):
    return Product(name, price, country_code)

def add_to_basket(basket, product, quantity=1):
    basket.add(product, quantity)
    
def buy_products(basket):
    results = f'{basket.total()} euros. Thank you for your purchase!'
    basket.clean()
    return results