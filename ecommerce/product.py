from .discount import Discount


class Product:
    def __init__(self, name, price, country_code='', discount:Discount=None):
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
        self.discount = discount.percent / 100 - 1 if discount else None
        if self.discount:
            self.discount = self.discount * - 1
    def __str__(self)-> str:
        country = self.country_code if self.country_code else 'Global'
        if self.discount:
            return f"{self.name} - {self.price} - {country} - {self.discount * 100}%"
        return f"{self.name} - {self.price} - {country}"
