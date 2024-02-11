from ecommerce.basket import Basket
from ecommerce.country import ListCountries, Country
from ecommerce.discount import Discount
from ecommerce.product import Product

def create_country_list()-> ListCountries:
    return ListCountries()

def select_country(country_list, country_code)-> Country:
    return country_list.select(country_code)

def create_country(name, code, symbol)-> Country:
    return Country(name, code, symbol)

def make_product(name, price, country_code='', discount:Discount=None)-> Product:
    return Product(name, price, country_code, discount)

def create_basket()-> Basket:
    return Basket()

def add_to_basket(basket:Basket, product:Product, quantity=1)-> None:
    basket.add(product, quantity)

def buy_products(basket:Basket)-> str:
    results = f'{basket.total()} euros. Thank you for your purchase!'
    basket.clean()
    return results
    
    